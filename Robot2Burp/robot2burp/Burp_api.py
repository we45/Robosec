import requests
from bs4 import BeautifulSoup
import subprocess
import time
import socket
import yaml
from time import gmtime, strftime, localtime



class Burp_api(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    #Running Burp API Service as a process in background
    def start_burp(self, burp_api_file,protocol="http",host_ip="127.0.0.1",port="8090",headless_mode="true",java_home="",):
        self.protocol=protocol
        self.host_ip=host_ip
        self.port=port
        self.headers={'Content-Type': 'application/json','Accept': '*/*'}
        if not java_home:
            subprocess.Popen("java -jar "+burp_api_file+" --port="+port+" --headless.mode="+str(headless_mode),shell=True, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, close_fds=True)

        if java_home:
            subprocess.Popen(java_home+"/bin/java -jar "+burp_api_file+" --port="+port+" --headless.mode="+str(headless_mode), shell=True, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, close_fds=True)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            result = sock.connect_ex((self.host_ip, int(self.port)))
            if result == 0:
                print "Port "+ self.port+ " is open\n"
                break
            # else:
            #     print "Port is not open"
        print  "Burp API Service Started\n"

    #Includes the specified URL in the Suite-wide scope.
    def include_scope(self,url):
        res=requests.put(self.protocol+'://'+self.host_ip+':'+self.port+'/burp/target/scope?url='+url,headers=self.headers)
        json_res = yaml.load(res.text)
        if res.status_code == 200:
            print '%s is added to the scope' %url
        else:
            print 'something is wrong with adding the url:%s' %url
            # print('state_code:' + str(json_res['status']) +'\n'+ 'Error:' + json_res['error']+'\n'+'Exception:'+json_res['exception']+'\n'+'Message:'+json_res['message'])
            print('state_code:' + str(json_res['status']) +'\n'+'Message:'+json_res['message'])


    #Excludes the specified Url from the Suite-wide scope.
    def exclude_scope(self,url):
        res=requests.delete(self.protocol+'://'+self.host_ip+':'+self.port+'/burp/target/scope?url='+url,headers=self.headers)
        json_res = yaml.load(res.text)
        if res.status_code == 200:
            print '%s is excluded from the scope' % url
        else:
            print 'something is wrong with excluding the url: %s' % url
            print('state_code:' + str(json_res['status']) +'\n'+'Message:'+json_res['message'])


    #Query whether a specific URL is within the current Suite-wide scope. Returns true if an url is in scope.
    def check_scope(self,url):
        res=requests.get(self.protocol+'://'+self.host_ip+':'+self.port+'/burp/target/scope?url='+url,headers=self.headers)
        json_res = yaml.load(res.text)
        if res.status_code ==  200:
            if json_res['inScope'] == True:
                print '%s is with in the scope' %url
            else:
                print '%s is not with in the scope' %url
        else:
            print('state_code:' + str(json_res['status']) +'\n'+'Message:'+json_res['message'])

    #Sends a seed URL to the Burp Spider tool. The baseUrl should be in Suite-wide scope for the Spider to run..
    def spider(self, url):
        body={'baseUrl': url}
        res = requests.post(self.protocol + '://' + self.host_ip + ':' + self.port + '/burp/spider',data=body)
        json_res = yaml.load(res.text)
        if res.status_code == 200:
            print '%s is added to spider' % url
        else:
            print 'something is wrong with adding the %s to the spider' % url
            print('state_code:' + str(json_res['status']) + '\n' + 'Message:' + json_res['message'])


    #Scans through Burp Sitemap and sends all HTTP requests with url starting with baseUrl to Burp Scanner for active scan.
    def active_scan(self, url):
        body={"baseUrl":url}
        res = requests.post(self.protocol + '://' + self.host_ip + ':' + self.port + '/burp/scanner/scans/active',data=body)
        json_res = yaml.load(res.text)
        if res.status_code == 200:
            print '%s is added to active scan' % url
        else:
            print 'something is wrong with adding the %s to the active scan' % url
            print('state_code:' + str(json_res['status']) + '\n' + 'Message:' + json_res['message'])


    #Deletes the scan queue map from memory, not from Burp suite UI
    def delete_active_scan(self, url):
        res = requests.delete(self.protocol + '://' + self.host_ip + ':' + self.port + '/burp/scanner/scans/active')
        json_res = yaml.load(res.text)
        if res.status_code == 200:
            print 'Active scan queue are removed from memory, not from Burp suite UI'
        else:
            print 'something is wrong with deleting the scn queue from the active scan'
            print('state_code:' + str(json_res['status']) + '\n' + 'Message:' + json_res['message'])


    #Returns an aggregate of percentage completed for all the scan queue items.
    def scan_status(self,url):
        while True:
            res=requests.get(self.protocol+'://'+self.host_ip+':'+self.port+'/burp/scanner/status',headers=self.headers)
            json_res = yaml.load(res.text)
            if res.status_code ==  200:
                if json_res['scanPercentage'] < 100:
                    time.sleep(5)
                    # print 'Scan is in progress:'+ str(json_res['scanPercentage'])
                else:
                    print  'Active Scan completed for the scope url:%s status:%s' %(url,str(json_res['scanPercentage']))
                    break
            else:
                print('state_code:' + str(json_res['status']) +'\n'+'Message:'+json_res['message'])



    #Returns all of the current scan issues for URLs matching the specified urlPrefix. Performs a simple case-sensitive text match, returning all scan issues whose URL begins with the given urlPrefix. Returns all issues if urlPrefix is null.
    def issue_result(self,url):
        res=requests.get(self.protocol+'://'+self.host_ip+':'+self.port+'/burp/scanner/issues?urlPrefix='+url,headers=self.headers)
        json_res = yaml.load(res.text)
        if res.status_code ==  200:
            # print '\033[1;32;0mIssues: \033[1;37;0m'
            print 'Total no of issue identified:'+ str(len(json_res['issues']))+'\n'
            for issue in json_res['issues']:
                print 'Issue Name:'+issue['issueName']+'\nIssue Url:'+issue['url']+'\nIssue Type:'+str(issue['issueType'])+'\nIssue severity:'+issue['severity']+'\nConfidence:'+issue['confidence']+'\n'
        else:
            print('state_code:' + str(json_res['status']) +'\n'+'Message:'+json_res['message'])


    #This will exit Burp Suite. Use with caution: the API will not work after this endpoint has been called. You have to restart Burp from command-line to re-enable te API.
    def stop_burp(self):
        res=requests.get(self.protocol+'://'+self.host_ip+':'+self.port+'/burp/stop',headers=self.headers)
        if res.status_code ==  200:
            # print '\033[1;32;0m Burp API Service is shutdown\033[1;37;0m'
            print 'Burp API Service is shutdown'
        else:
            json_res = yaml.load(res.text)
            print('state_code:' + str(json_res['status']) +'\n'+'Message:'+json_res['message'])


    #Returns details of items in the Burp suite Site map. urlPrefix parameter can be used to specify a URL prefix, in order to extract a specific subset of the site map.
    def sitemap(self,url):
        res = requests.get(self.protocol + '://' + self.host_ip + ':' + self.port + '/burp/target/sitemap?urlPrefix='+url, headers=self.headers)
        json_res = yaml.load(res.text)
        if res.status_code == 200:
            # print '\033[1;32;0mSitemap: \033[1;37;0m'
            print 'Total no of static url identified on the scope url:' + str(len(json_res['messages']))
            for site in json_res['messages']:
                 print 'Url:'+site['url']+'\nStatus Code:'+str(site['statusCode'])+'\n'
        else:
            print('state_code:' + str(json_res['status'])+'\n'+ 'Message:' + json_res['message'])

    #This will restore Burp's state with an empty one.
    # def reset_burp(self):
    #     res = requests.get(self.protocol + '://' + self.host_ip + ':' + self.port + '/burp/reset', headers=self.headers)
    #     json_res = yaml.load(res.text)
    #     if res.status_code == 200:
    #         print 'Burp state is restored'
    #     else:
    #         print('state_code:' + str(json_res['status']) + '\n' + 'Message:' + json_res['message'])



    #This will restore Burp's state with an empty one
    def generate_report(self,url,report_name,formats=[]):
        for report_format in formats:
            res = requests.get(self.protocol + '://' + self.host_ip + ':' + self.port + '/burp/report?urlPrefix=' + url + '&reportType=' + report_format,headers=self.headers)
            if res.status_code == 200:
                output=res.text
                if report_format.lower() == "html":
                    output = BeautifulSoup(output, 'lxml')
                elif report_format.lower() == "xml":
                    output = BeautifulSoup(output, 'xml')
                report= open("./results/"+report_name+"."+report_format.lower(),'w')
                report.write(str(output))
                report.close()

            else:
                json_res = yaml.load(res.text)
                print('state_code:' + str(json_res['status']) + '\n' + 'Message:' + json_res['message'])

    #Burp suite project-level configuration is loaded from the given JSON string.
    def burp_config(self,config):
        with open(config) as yml:
            cfg = yaml.load(yml)
        value={"configAsJson":cfg}
        res = requests.put(
            self.protocol + '://' + self.host_ip + ':' + self.port + '/burp/configuration',data=value)

        if res.status_code == 200:
            print '%s burp configuration file is updated' %config

        else:
            json_res = yaml.load(res.text)
            print('state_code:' + str(json_res['status']) + '\n' + 'Message:' + json_res['message'])

    def orchy_webhook(self,report_name,auth_token,webhook_url,engagement_id=''):
        req_headers={'Authorization':'Token '+auth_token,'X-Engagement-ID':engagement_id}
        files={'file':open("./results/"+report_name+"."+"xml",'r')}
        req = requests.post(webhook_url,headers=req_headers,files=files)
        if req.status_code == 200:
            print "Result pushed successfully"
            with open('./results/orchy_log.json','a') as orchy_log:
                log_data="["+strftime("%Y-%m-%d %H:%M:%S", localtime())+"]: "+req.content
                orchy_log.write(log_data +'\n')
                orchy_log.close()
        else:
            with open('./results/orchy_log.json','a') as orchy_log:
                log_data="["+strftime("%Y-%m-%d %H:%M:%S", localtime())+"]: "+req.content
                orchy_log.write(log_data+'\n')
                orchy_log.close()


