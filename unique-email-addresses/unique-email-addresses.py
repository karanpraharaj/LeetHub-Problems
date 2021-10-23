class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        a = []
        for i in range(len(emails)):
            user_name = emails[i].split('@')[0].split('+')[0]
            user_name_dot_filtered = ''.join(user_name.split('.'))
            domain_name = emails[i].split('@')[1]
            
            unique = user_name_dot_filtered+"@"+domain_name
            
            if unique not in a:
                a.append(unique)
    
        return len(a)
            