# getBlackboardDirectory
A command line tool for downloading Blackboard course directories.

## How to find your session ID:

### 1. Open Google Chrome and log into Blackboard with your credentials.

![Login](https://media.discordapp.net/attachments/681862516279738391/716121719265296404/unknown.png?width=2052&height=980)

### 2. Go to ``blackboard.SCHOOL-NAME.edu/learn/api/public/v1/courses``

Replace ``SCHOOL-NAME`` with your college or university's domain name:
![enter image description here](https://media.discordapp.net/attachments/681862516279738391/716123511491395615/unknown.png)
This will take you to a page that looks like this:
![enter image description here](https://media.discordapp.net/attachments/681862516279738391/716125495472816209/unknown.png?width=1276&height=1003)
### 3. Click ``Ctrl + Shift + I`` on your keyboard or left click and select ``Inspect``
![enter image description here](https://www.wikihow.com/images/0/0a/Inspect-Element-on-Chrome-Step-7.jpg)
This will open Chrome DevTools:
![enter image description here](https://media.discordapp.net/attachments/681862516279738391/716126196181499966/unknown.png?width=1414&height=1002)

### 4. Select ``Network`` from the Chrome DevTools menu
![enter image description here](https://media.discordapp.net/attachments/681862516279738391/716126841169248276/unknown.png)

### 5. Hit ``Ctrl + R`` on your keyboard.

The following list will pop up:
![enter image description here](https://media.discordapp.net/attachments/681862516279738391/716127791829221386/unknown.png?width=1352&height=1002)
### 6. Select the ``Courses`` item and copy ``s_session_id`` from ``Request Headers``
Copy the string of letters/numbers highlighted in light blue down below, but from your own page.
![enter image description here](https://media.discordapp.net/attachments/681862516279738391/716128630391963648/unknown.png)

### 7. Save ``s_session_id`` in a secure location. You will need it to run the program.
