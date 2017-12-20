import nessrest6
from bs4 import BeautifulSoup


class Robot2nessus(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def nessus_login(self,server_ip,username,password,ssl=True):
        if ssl == "True":
            self.scan = nessrest6.Scanner(url=server_ip, login=username, password=password, insecure=False)
        elif ssl == "False":
            self.scan = nessrest6.Scanner(url=server_ip, login=username, password=password, insecure=True)

    def set_scan_policy(self,policy_name=''):
        if policy_name:
            self.scan.policy_set(name=policy_name)

    def create_scan(self,hosts,folder_name="My Scans",scan_name="",scan_template="custom",schedule=''):
        if hosts and not schedule:
            self.scan.scan_add(targets=hosts,tag_name=folder_name,template=scan_template,name=scan_name)

        elif hosts and schedule:
            self.scan.scan_add(targets=hosts,tag_name=folder_name,template=scan_template,name=scan_name,start=schedule)

    def run_scan(self):
        self.scan.scan_run()

    def scan_results(self):
        self.scan.scan_results()

    def export_scan_results(self,report_name,report_formats=[],report_category="",db_pass=""):
        for report_format in report_formats:
            output=self.scan.download_scan(export_format=report_format,chapters=report_category,dbpasswd=db_pass)
            report= open("./results/"+report_name+"."+report_format,'w')
            report.write(output)
            report.close()

    def download_scanned_report(self,folder_name,scn_name,report_name,report_formats=[],report_category="",db_pass=""):
        for report_format in report_formats:
            output=self.scan.download_report(tag_name=folder_name, scan_name=scn_name, export_format=report_format, chapters=report_category, dbpasswd=db_pass)
            if report_format == "html":
                output=BeautifulSoup(output,'lxml')
            if report_format == "nessus":
                output=BeautifulSoup(output,'xml')
            report= open("./results/"+report_name+"."+report_format,'w')
            report.write(str(output))
            report.close()