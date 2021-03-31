import os
import getpass
os.system("tput setaf 2")
print("\t\t\t Welcome to My Menu Program")
os.system("tput setaf 7")
print("\t\t\t-----------------------------")

passwd = getpass.getpass("Enter your password :")
if passwd != "redhat":
    print("password incorrect")
    exit()

def intro():
    os.system("tput setaf 2")
    print("\t\t\t Welcome to My Menu Program")
    os.system("tput setaf 7")
    print("\t\t\t-----------------------------")


def nn():
      import os
      IP = input("\t\t\tGive your IP:")
      folder = input("\t\t\tFolder name for namenode:")
      os.system("rm -rf {}".format(folder))
      os.system("mkdir {}".format(folder))
      port = input("\t\t\tInsert Port Number at which you want to run namenode service:")

      hdfs = open("/etc/hadoop/hdfs-site.xml" , "w")
      data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(folder)
      hdfs.write(data)

      core = open("/etc/hadoop/core-site.xml", "w")
      data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(IP,port)
      core.write(data)
      

def start_nn():
      import os
      f=input("Enter directory name for formatting:")
      os.system("hadoop namenode -format {}".format(f))
      os.system("hadoop-daemon.sh start namenode")

def stop():
    print('''\t\t\t1.Stop Namenode
    \t\t\t2.Stop Datanode
    
    \t\t\t3.Admin report
    \t\t\t4.Process running
    \t\t\t5.Back\n''')

    ch=input("Enter your choice: ")
    if int(ch)==1:
        os.system("hadoop-daemon.sh stop namenode")
    elif int(ch)==2:
        os.system("hadoop-daemon.sh stop datanode")
    elif int(ch)==3:
        os.system("hadoop dfsadmin -report")
    elif int(ch)==4:
        os.system("jps")
    elif int(ch)==5:
        mainmenu()

def dn():
      import os
      IP = input("\t\t\tGive IP of your namenode:")
      folder = input("\t\t\tFolder name of datanode:")
      os.system("rm -rf {}".format(folder))
      os.system("mkdir {}".format(folder))
      port = input("\t\t\tInsert Port Number at which you want to run namenode service:")

      hdfs = open("/etc/hadoop/hdfs-site.xml" , "w")
      data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(folder)
      hdfs.write(data)

      core = open("/etc/hadoop/core-site.xml", "w")
      data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(IP,port)
      core.write(data)

def start_dn():
      import os
      os.system("hadoop-daemon.sh start datanode")


def webserver():
      import os
      os.system("yum install httpd")
      print("Webserver installed sucessfully")
      os.system("systemctl start httpd")



def partition():
	os.system("clear")
        
	print('''\t\t\t1.Create Static partition
        
        \t\t\t2.Create LVM partition\n''')

	ch=input("\t\t\tEnter your choice:")
	if int(ch) == 1:
		m=input("Enter folder for which you want to create partition:")
		n=input("Enter folder to mount:")
		os.system("fdisk {}".format(m))
		os.system("mkfs.ext4 {}".format(m))
		os.system("mount {} {}".format(m,n))

	elif int(ch) == 2:
		while True:
			os.system("tput setaf 2")
			print("""\n 		0.fdisk\n	 	1.create physical partition's\n 		2.create volume group(vg)\n 		3.Create Logical volume(LV)\n 		4.Display\n	 	5.format lv\n 		6.make storable drive\n 		7.mount\n 		8.Extend\n 		9.resize\n 		10.Back\n""") 


			k=input("enter ur choice \n")

			if int(k)==0:
				os.system("fdisk -l")

		
			elif int(k)==1:
				
				os.system("pvcreate {}".format(input("enter drive location\n")))


			elif int(k)==2:
				os.system("vgcreate {} {} {}".format(input("new vg name\n"),input("enter pv 1 drive location\n"),input("enter pv 2 drive location\n")))


			elif int(k)==3:
				os.system("lvcreate --size {} --name {} {}".format(input("enter required size\n"),input("enter lv name\n"),input("enter vg name")))


			elif int(k)==4:

				while True:
					print(""" 	1.for pv display\n 	2.for vg display\n 	3.for lv display\n	4.Back\n 	""")


					m=input("select your choice\n")
					if int(m)==1:
						os.system("pvdisplay {}".format(input("enter pv name\n")))
					elif int(m)==2:
						os.system("vgdisplay {}".format(input("enter vg name\n")))

					elif int(m)==3:
						os.system("lvdisplay {}/{}".format(input("enter vgname\n"),input("input lvname\n")))
						
					elif int(m)==4:
						partition()
						

			elif int(k)==5:
				os.system("mkfs.ext4 /dev/{}/{}".format(input("vg name\n"),input("lv name\n")))


			elif int(k)==6:
				os.system("mkdir /{}".format(input("enter folder name\n")))

		
			elif int(k)==7:
				os.system("mount /dev/{}/{} /{}".format(input("enter vg name\n"),input("enter lv name\n"),input("enter folder name\n")))


			elif int(k)==8:
				os.system("lvextend --size +{} /dev/{}/{}".format(input("enter required size\n"),input("enter vg name\n"),input("enter lvname\n")))


			elif int(k)==9:
				os.system("df -hT")
			elif int(k)==10:
				mainmenu()

		
def docker():
      import os
      repo = open("/etc/yum.repos.d/docker.repo" , "w")
      data = '''[docker]
      baseurl=https://download.docker.com/linux/centos/7/x86_64/stable
      gpgcheck=0'''
      repo.write(data)
      os.system("yum install docker-ce --nobest  -y")
      print("Docker installed successfully")
      
def docker_service():

    while True:
       intro()
       print('''\t\t\t1.Start docker service
	\t\t\t2.Docker images
      	\t\t\t3.Docker running status
      	\t\t\t4.Pull OS
 	\t\t\t5.Launch 0S
      	\t\t\t6.OS running
      	\t\t\t7.Back to main menu\n''')

       os.system("tput setaf 2")
       ch=input("\t\t\t Enter your choice:")
       if int(ch) == 1:
          os.system("systemctl start docker")
       elif int(ch) == 2:
          os.system("docker images")
       elif int(ch) == 3:
          os.system("systemctl status docker")
       elif int(ch) == 4:
           os.system("docker pull {}".format(input("Enter os name you want to install")))
       elif int(ch) == 5:
           os.system("docker run -it --network host {}".format(input("Enter image name:")))
       elif int(ch) == 6:
           os.system("docker ps")
       elif int(ch) == 7:
           mainmenu()

def Linux():
  while True:
     os.system("tput setaf 6") 
     print('''\t\t\t1.Run Date
     \t\t\t2.Run Calendar
     \t\t\t3.Show IP address
     \t\t\t4.Show RAM
     \t\t\t5.Memory
     \t\t\t6.Who am I?
     \t\t\t7.Current Directory
     \t\t\t8.View contents of directory
     \t\t\t9.Back\n''')

     ch=input("Enter your choice:")
     if int(ch)==1:
         os.system("date")
     elif int(ch)==2:
         os.system("cal")
     elif int(ch)==3:
         os.system("ifconfig")
     elif int(ch)==4:
         os.system("free -m")
     elif int(ch)==5:
         os.system("df -h")
     elif int(ch)==6:
         os.system("whoami")
     elif int(ch)==7:
         os.system("pwd")
     elif int(ch)==8:
         os.system("ls")
     elif int(ch)==9:
         mainmenu()


def AWS():
	while True:    
		intro()
		print('''\t\t\t1.Create Key Pair
		\t\t\t2.Create Security Group
		\t\t\t3.Launch instance
		\t\t\t4.Create Volume
		\t\t\t5.Attach Volume
		\t\t\t6.Create Bucket
		\t\t\t7.Create Cloudfront Distribution
	       
		\t\t\t8.Go to main menu''')

		r=input("Enter your choice :")
		if int(r) == 1:
			os.system("aws ec2 create-key-pair --key-name {}".format(input("Enter key name:")))		

		elif int(r)==2:
			os.system("aws ec2 create-security-group --group-name {} --description {}".format(input("enter group name\n"),input("enter group description\n")))


		elif int(r)==3:
			os.system("aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-group-ids {} --count 1 --subnet-id {}".format(input("enter image id\n"),input("enter instance type\n"),input("enter key name\n"),input("enter security group id\n"),input("enter subnet id\n")))


		elif int(r)==4:
			os.system("aws ec2 create-volume --availability-zone {} --volume-type {} --size {}".format(input("enter availability zone \n"),input("enter volume type \n"),input("enter size \n")))


		elif int(r)==5:
			os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device {}".format(input("enter instance id\n"),input("enter volume id \n"),input("enetr device name \n")))


		elif int(r)==6:
			os.system("aws s3api create-bucket --bucket {} --create-bucket-configuration LocationConstraint=ap-south-1 --acl {}".format(input("enter unique name of bucket \n"),input("enter readable view i.e acl\n")))
						
						

		elif int(r)==7:
			os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazon.com".format(input("enter bucket name")))

		elif int(r)==8:
			mainmenu()
						
					
    
def mainmenu():

   while True:
      intro() 
      import os
      os.system("tput setaf 4")
      print('''\t\t\t 1.Configure Hadoop Namenode
      \t\t\t 2.Configure Hadoop Datanode
      \t\t\t 3.Create Partition
      \t\t\t 4.Configure Webserver
      \t\t\t 5.Configure Docker
      \t\t\t 6.Amazon Web Service
      
      \t\t\t 7.Hadoop services
      \t\t\t 8.Basic Linux commands
      
      \t\t\t 9.Exit program\n''')
 
      ch=input("\t\t\tEnter your choice: ")

      if int(ch) == 1:
          nn()
          start_nn()

      elif int(ch) == 2:
          dn()
          start_dn()

      elif int(ch) == 3:
          partition()  

      elif int(ch) == 4:
          webserver()

      elif int(ch) == 5:
          docker()
          docker_service()
     
      elif int(ch) == 6:
          AWS()

      elif int(ch) == 7:
          stop()

      elif int(ch) == 8:
          Linux()

      elif int(ch) == 9:
          exit()

mainmenu() 
