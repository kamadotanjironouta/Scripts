#!/usr/bin/env python
'''
Scripts to Generate Syscalls functions for nasm
'''
import bs4
import requests

URL = "https://filippo.io/linux-syscall-table/"

FORMAT = '''\
_{}: ; ref ⇒ {}
    mov rax, {}
    syscall
    ret\n
'''

def generate():
    '''
    ^^
    '''

    with requests.get(URL) as req:
        res = req.text

    table = bs4.BeautifulSoup(res).find('table', {'class': 'tbls-table'}).find_all('tr', {'class': 'tbls-entry-collapsed'})
    with open("./syscalls.nasm", "w") as _f:
        for entry in table:
            td = entry.find_all('td')
            syscall_num = td[0].text
            syscall_name = td[1].text
            syscall_ref = td[3].text
            _f.write(FORMAT.format(syscall_name, syscall_ref, syscall_num))



if __name__ == "__main__":
    generate()
