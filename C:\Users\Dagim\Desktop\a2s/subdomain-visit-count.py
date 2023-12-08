class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        Domain_info = {}

        for cpdomain in cpdomains:
            split_domain = cpdomain.split(' ')
            ndomain = int(split_domain[0])
            mdomain = split_domain[1]
            subdomains =mdomain.split('.')

            for i in range(len(subdomains)):
                domain = '.'.join(subdomains[i:])
                if domain not in Domain_info:
                    Domain_info[domain] = 0
                Domain_info[domain] += ndomain
        result = []
        for domain,count in Domain_info.items():
            result.append(str(count)+ ' ' + domain)
        return result
                





        