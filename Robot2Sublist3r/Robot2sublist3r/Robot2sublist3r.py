import sublist3r
import logging

class Robot2sublist3r(object):

    def __init__(self):
        self.subdomain_count=''

    def enumerate_subdomain(self,target, threads_no, output_file, ports=None, silent_mode=False, verbose=False, bruteforce=False, engines=None):
        results=sublist3r.main(domain=target,threads=threads_no, savefile="results/"+output_file, ports=ports, silent=silent_mode, verbose=verbose,
                   enable_bruteforce=bruteforce, engines=engines)
        self.subdomain_count=len(results)
    def get_subdomain_count(self):
        return str(self.subdomain_count)



