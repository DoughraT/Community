HOW TO RUN WEBSITE:

1. Install Python 
2. Install Gitbash (https://gitforwindows.org/)
3. Download folders from Github
4. Unzip downloaded package
5. Open Gitbash and locate Community-main
6. In dir with community_website & virt run the following command to activate the virtual environment:
	source virt/Scripts/activate

7. pip install django (for latest version)
8. pip install pillow
9. Move into community_website folder - should see the manage.py file
10. Run the server using the following command: 
	python manage.py runserver

11. On web browser go to localhost:8000
12. Website should be up
	To access Admin page: goto localhost:8000/admin
		Admin Username: admin
		Admin Password: admin@123456