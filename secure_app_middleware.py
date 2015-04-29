import traceback, sys, time, re
from django.contrib.sessions.backends.db import SessionStore
from secure_app.models import Request, Filter
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
import logging
from garepair import GaRegexCreator
import pprint
from django.shortcuts import render
from django.test.client import Client
logger = logging.getLogger(__name__)
from delta3 import views
#sh = logging.StreamHandler()
#logger.addHandler(sh)
global isEvil, flag
isEvil = False
flag = False
class Repair(object):
    '''
    Repair a fatal crash that occurs by creating a regex filter to
    allow "good" input and block "bad" input. Bad input is input that 
    causes a fatal crash.

    The current design is vulnerable to sophisticated training data poisioning
    such that a malicious user inserts bad data that gets counted as good. 
    When the regex is created, it cant tell the difference between good and 
    bad.
    '''
    REQUEST_ID = "req_id"

    def save_request(self,sessionid, timestamp, url_path, param_map):
        '''
        Save every request so it can be later used for training. 
        Each requst name and value is stored
        '''
        #TODO shouldnt store name=value pair duplicates
        is_good = True
        # TODO Why is there a delete_seleted condition? what does it do
        if len(param_map) != 0 and "delete_selected" not in str(param_map):
            for key, value in param_map.iteritems():
                r = Request(
                        timestamp=timestamp, 
                        sessionid=sessionid,
                        url_path=url_path, 
                        is_good=is_good, 
                        key=str(key), 
                        value=str(value)
                    )
                r.save()
                logger.info("SAVE time=" + timestamp + " path=" + url_path + " " + str(key) + "=" + str(value) )

    def has_evil_input(self, url_path, param_map):
        # Filter requests
        # Check if Filter objects' url path, form field name, and regex matches the request
        global isEvil
        for f in Filter.objects.filter(url_path=url_path):
            field_name = getattr(f, 'field_name')
            regex = getattr(f, 'regex_filter')
            print "Regex:",regex
            requested_value = param_map[field_name]

            logger.debug("====Field:" + field_name + " filter:" + regex + " for value:" + requested_value +"====")
            # The filters are inclusions, if the input doesn't
            # match the accecpt regex then its malicious 
            if not re.match(regex, str(requested_value)):
                isEvil = True
                break
        return isEvil

    def get_param_map(self, request):
        # Log GET requests
        if request.method == 'GET':
            param_map = request.GET
        # Log POST requests
        elif request.method == 'POST':
            param_map = request.POST
        return param_map

    def taint_input(self, param_map):
        '''
        Taint the input so we can determine if one of these inputs
        caused an exception 
        '''
        #TODO implement me
        pass

    def process_request(self, request):
        if not request.session.exists(request.session.session_key):
            logger.debug("creating new session")
            request.session.create()
        sessionid = request.session.session_key
        logger.debug(sessionid)
#        pprint.pprint(request.META, stream=sys.stderr)
        timestamp = str(time.time())
        # we define a request id and tie it to the 
        # request object so there is a way during an exception 
        # we can retrieve information saved from the database
        request.META[self.REQUEST_ID] = timestamp 
        url_path = str(request.get_full_path())
        param_map = self.get_param_map(request)
        global isEvil
        isEvil = False
        if param_map and flag == False:
           self.taint_input(param_map)
           if self.has_evil_input(url_path, param_map):           
               return HttpResponse("Evil input detected -_-")
           else:
                #save to the database
               self.save_request(sessionid, timestamp, url_path, param_map) 
        return

    def get_request_data(self, param_name, is_good):
        return [r.value for r in Request.objects.filter(key = param_name, is_good = is_good)]

    def _remove_poisoned_data(self, sessionid):
        '''
        If an exception occurs we want to remove all the data entered by 
        this malicous user because it may have been poisoned
        '''
        Request.objects.filter(sessionid=sessionid, is_good=True).delete() 


    def process_exception(self, request, exception):
        sessionid = request.session.session_key
        #try:
        id = request.META[self.REQUEST_ID]
        logger.debug("Processing exception..." + id + " " + sessionid)  
        s = str(exception)
        url_path = str(request.get_full_path())
    
        # From interpreter get name that caused exception
#TODO REMOVE ME, I AM HERE FOR TESTING
        vulnerable_name = "searchterm" 
        r = s[s.index("'"):]
        print r
        if 'register' in url_path:
            vulnerable_name = 'age'
        # Use request to query the database, so we can update the input to evil
        print "timestamp:",id, url_path
        evil_req = Request.objects.filter(timestamp=id, url_path=url_path, key=vulnerable_name)[0]
        evil_req.is_good = False
        evil_req.save()
        self._remove_poisoned_data(sessionid)

        # Query for benign and malicious input
        data_evil = self.get_request_data(vulnerable_name, False)
        #logger.debug("================EVIL=================")
        #logger.debug(str(data_evil))
        data_benign = self.get_request_data(vulnerable_name, True)
        #logger.debug("================GOOD=================")
        #logger.debug(str(data_benign))

        # Pass these two data sets to the GA
        ga = GaRegexCreator(data_evil, data_benign, verbose=False)
        regex  = ga.create_regex()

        filter, created = Filter.objects.get_or_create(url_path=url_path,field_name=vulnerable_name) 
        filter.regex_filter = regex
        filter.save()

        logger.debug("Filter " + regex + " has been applied for " + vulnerable_name + " in ") 
        try:        
            type, value, tb = sys.exc_info()
            logger.debug(type)
            logger.debug(value)
            logger.debug(traceback.extract_tb(tb))
            logger.info("TAken here")
        except Exception as e:
            print e
            #del tb
            # Save the regex so it can filter evil things next time
        #except Exception as e:
        #    logger.error("Unknown exception " + str(e))

        #finally:
#            return HttpResponsePermanentRedirect(request.get_full_path().split("?")[0])
    #     pass        
    #False-positive-check for the Repair check
    def process_response(self, request, response):
        if response.status_code == 200 and isEvil == True:
            print "======False Positive check========"
            global flag
            flag = True
            g = self.get_param_map(request)
            original_path = str(request.get_full_path())
            c = Client()
            respond = c.get(original_path , g)
            if respond.status_code == 200:
                response = respond       
        return HttpResponse(response)    


            
            

            

