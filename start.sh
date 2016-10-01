cd /home/uri/DLI/server/; python -m SimpleHTTPServer 7999 &
VBoxManage startvm cuckoo1 --type headless &
cd /home/uri/cuckoo/web/; python manage.py runserver 7998 &
cd /home/uri/DLI/; python file_proxy.py
