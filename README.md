# Car Catalog Project
## Summary
The Car Catalog Application is my project associated with the Item Catalog project from the Udacity Full-Stack Nanodegree program. The goal of the project was to build a Web application using Flask and SQLAlchemy along with OAuth for authentication and authorization. In this project I wanted to differentiate from other Item Catalog projects by building a unique project that would employ real world application.


## Requirements
* Install [Virtual Box](https://www.virtualbox.org/)
* Install [Vagrant](https://www.vagrantup.com/)
* Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository

Please use the additional Information below to setup the environment for this project:

### Git

If you don't already have Git installed, [download Git from git-scm.com.](http://git-scm.com/downloads) Install the version for your operating system.

On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash).  
(On Mac or Linux systems you can use the regular terminal program.)

You will need Git to install the configuration for the VM.

### VirtualBox

VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

**Ubuntu 14.04 Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need.

### Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.


## Running the Program

**Windows:** Use the Git Bash program (installed with Git) to get a Unix-style terminal.  
**Other systems:** Use your favorite terminal program.

1. From within the Vagrant folder you downloaded on to your machine use the command  `vagrant up` to set up the Virtual Machine.
2. Use `vagrant ssh` to log into your Virtual Machine.
3. Navigate into the Vagrant directory using `cd /vagrant`
4. From the terminal run `git clone https://github.com/jjp601/Car_Catalog_Project catalog`. This will provide you with all of the source code and files to get the Flask application up and running.
5. From within the catalog directory please ensure the directory has a static folder with the styling and image files, a templates folder with all html template files, a **client_secrets.json**, a **db_setup.py**, a **cars.py**, and a **app.py** file.
6. Run `python db_setup.py` to initialize the database.
7. Next, run `python cars.py` to populate the database.
8. Run `python app.py` to run the Flask web server. The Car Catalog application can the be viewed in your browser at **http://localhost:5000**.
9. Once you have the application running you will be able to login using your Facebook account. You can add, edit, and delete your own car dealerships, add, edit, and delete new cars, upload an image with URL and view other dealerships.

## Future Enhancements

Plan to make the following enhancements:

* Add functionality to allow users to upload a photo.
* Add a path and functionality to allow users to Buy another Dealer's car. (Note: The Buy button currently has no functionality)
* Add a path and functionality to allow users to Lease another Dealer's car. (Note: The Lease button currently has no functionality)
