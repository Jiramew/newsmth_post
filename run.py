from newsmth.newsmth import SmthPost

__author__ = 'jiramew'

if __name__ == '__main__':
    sp = SmthPost()
    if sp.login():
        sp.post_job()
