__Django project__

#This is the beginners guid for working with django framework. So let's get started.

#
#
First of all we have to install the django using python -m pip install django.
In my case it is already installed and we can check its version also.
Then follow the commands given below then you will see a folder is created with some pre-existing folders and python scripts
#
![step-1](https://github.com/keshavgbpecdelhi/my_first_django_project/blob/master/Screenshot%20(41)_LI.jpg)

#
Follow the steps by giving commands.
#
![step-2](https://github.com/keshavgbpecdelhi/my_first_django_project/blob/master/Screenshot%20(43).png)

#
Now this is my manage.py which I have opened in notepad++ but you can use your favorite editor.
#
![step-3](https://github.com/keshavgbpecdelhi/my_first_django_project/blob/master/Screenshot%20(44).png)

#
The folder name my_django is created by using the command of startapp which you can look above in cmd then all these files are autopopulated. Now, look how our python scripts are created.
#
![step-4](https://github.com/keshavgbpecdelhi/my_first_django_project/blob/master/Screenshot%20(45).png)

#
Now here is what we write in h1 tag is going to be shown by using HttpResponse module. This is essentially every time modification type script. Here we can create as much functions we require so as to create more pages in localhost.
#
![step-5](https://github.com/keshavgbpecdelhi/my_first_django_project/blob/master/Screenshot%20(46).png)

#
Now to show up that content written between h1 tags we have to create a urls.py file inside our my_django folder and we have to do these changes as shown below. We have not given any path so it will be shown in our starting localhost, we can even specify its path something like '/project' but for now let's take it as it is.
#
![step-6](https://github.com/keshavgbpecdelhi/my_first_django_project/blob/master/Screenshot%20(47).png)

#
Now coming to the main urls.py we have to specify that my_django path here below the admin path. This is a good practice to segregate codes in small parts for less confusion in future.
#
![step-7](https://github.com/keshavgbpecdelhi/my_first_django_project/blob/master/Screenshot%20(48).png)

#
Are you ready! We are gonna start our localhost by just a single command in cmd i.e. python manage.py runserver. This will show us the localhost ip address which is awesome because this only occurs when we have performed everything correctly.
#
![step-8](https://github.com/keshavgbpecdelhi/my_first_django_project/blob/master/Screenshot%20(49).png)

#
Now writing that ip in your browser or simply writing localhost:8000 will run our simple django project.
#
![step-9](https://github.com/keshavgbpecdelhi/my_first_django_project/blob/master/Screenshot%20(50).png)

#
#
![step-10](https://github.com/keshavgbpecdelhi/my_first_django_project/blob/master/Screenshot%20(51).png)

#
Get! Set! Go! After pressing enter we are now able to see that h1 tag line in the page. See how we can start using django for our projects. 
#
![step-11](https://github.com/keshavgbpecdelhi/my_first_django_project/blob/master/Screenshot%20(53).png)

#
Probably you were thinking that the same line written in html will also show up in browser..but wait there is lot more to cover & there are tons of benefits for using django in your projects as early you go further you will be able to feel its benefits.
#
