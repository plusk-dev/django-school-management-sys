from dhooks import Webhook

hooks = {
	'class-6': 'https://discord.com/api/webhooks/793734361962905600/hg5PU6BjDAjMYBGI0hAt42YQnxuXYkEXNMA4bbkI09tCc_KYolUnqSrO0_2XwXvyUN_B',
	'class-7': 'https://discord.com/api/webhooks/793734484616675338/cDHD5DpPeCUio4f0D6TvRM_JaHGIsd4VFGdWB6Frxa8nykHfgXxqMjOpXg_3Zdrzv0YJ',
	'class-8': 'https://discord.com/api/webhooks/793734584650563594/dF5PPG3MCNCYKs1qxXcWaLsC2VIiQSYgz0LrQTybrAruBn5ievs7sJF55se-cuzzERzQ',
	'class-9': 'https://discord.com/api/webhooks/793734666644881408/0ttWiIzNJ1BlwkVFUukZ2Y4QCBsT6NYiakIJ0YHXvTfhKPnYYNinJn-yfItGGK60Qi9X',
    'class-10': 'https://discord.com/api/webhooks/793539291677589515/JEH1i7elBkesfIo_ppMISh9drbK_eWhUmKoPZEgGAYxdnvL6U7B5Ps8lSXw6L-e01lEI',
    'class-6-teachers': 'https://discord.com/api/webhooks/793739432112554044/HgQSJAx8hl4IkswQOJ1ayXk7iT-p-oYi85bTqD7c51tjV-eFpwFMgx_ne8WIQ2vuFjcZ',
    'class-7-teachers': 'https://discord.com/api/webhooks/793739564372066324/rGy1X8k6DHC6hhWdvniliGsjpT1EibJI1p3cMlAZN07yPfUXUj66CHhOZoIIfLMhbfuc',
    'class-8-teachers': 'https://discord.com/api/webhooks/793739664053239829/RVHBJf3BbRcJEARZgK2LDE706thzjHVn97zJtKoQNoHLSpIxzxJ9BDq5XREwM3cRnaat',
    'class-9-teachers': 'https://discord.com/api/webhooks/793739769309560882/a9bSGgKiPsug8P6mcfaWQizoZha-ikqwrJ8sVWLqU0UEi_alWt78Po0uPjiwYLtQ8C0K',
    'class-10-teachers': 'https://discord.com/api/webhooks/793739939111501854/vlg5PGmHV9Fgx5CzFeLfmdWEtW5wtEIhrQCWKk6XEzxUhaqc9cAJ4ufN71QUqDFhBX17',
    'exam-notifications': 'https://discord.com/api/webhooks/793528586954211368/d2scb9cDlMDPiyK59R_r0nWBK8w8u1ROu9sqnRjmr0ub9c4lwbVzNKdZ4Y2h8gW9NlbX',
    'teachers-general': 'https://discord.com/api/webhooks/793526176349683722/p5w3G6UvZsLbN0ZQ9SHAMhGyMXmPwOG2Xf4m9OhsiQeNPZ8Ax5M-aXNr5TfmzZUhmQ7z',
    'announcements': 'https://discord.com/api/webhooks/793533399494950951/oLbYVMRmI5Lnljw1IOLOqfEScLmuT7xsb4rqPQVszXwPdwZxsLR336vffAar1Feo8l5m',
}

def send(to, message):
	hook = Webhook(hooks[to])
	hook.send(message)

