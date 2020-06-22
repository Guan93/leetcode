#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#


# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def convert_local(local):
            try:
                end = local.index('+')
            except ValueError:
                end = len(local)
            return ''.join(local[:end].split('.'))

        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            unique_emails.add(convert_local(local) + '@' + domain)

        return len(unique_emails)


# @lc code=end
