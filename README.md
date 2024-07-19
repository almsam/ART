<a name="readme-top"></a>



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/almsam/data-analysis-project-revisited">
    <img src="public/img/minerals logo.png" alt="Logo" width="180" height="180">
  </a>

<h3 align="center">Discord Clone Software Engineering Project</h3>

<p align="center">
  <strong>Mission Statement</strong><br>
" Our mission is to create a messaging platform that offers robust communication features similar to Discord, enabling users to connect seamlessly across servers and direct messages. "</p>


</div>

## About the project

  During my third year of undergrad, My group of 5 was tasked with building a full application (with front end & back end) to demonstrate our abilities to implement good software engineering practices. Frankly: this project fell far from my expectations & was far from my finest work, but I still feel publically archiving my dumpsterfire will do me well in showing anyone on this repo how much progress I have made in this adventure of learning to code & the lessons I have learnt along the way.

<!-- SUMMARY -->

## Executive Summary
Our Discord clone aimed to deliver a comprehensive messaging system where users could join servers, send and receive messages, & manage communication efficiently. With features like server and channel management, DM's, file sharing, & real-time notifications, our platform ensures an engaging user experience. Developed in Flask for Python with a focus on functionality, this project worked well with demonstrating the importance of robhust engineering practcies.

<!-- FEATURES -->

## Features

### Main Page
- **Search for servers and channels** from the root page `/` and the main server directory `/listservers`.
- By default, all servers are listed on `/listservers`.
- Most pages have a navigation bar fixed to the top which lists the username of the current user.

### Messaging System
- **Servers and Channels**
  - Join servers and access text and voice channels.
  - Create and manage servers, including user roles and permissions.
  - Create, edit, and delete channels within servers (if admin permissions exist).
  - Add server icons and search for servers and channels.
  - Generate invite links for servers and channels.
- **Direct Messaging and Friend System**
  - Send and receive direct messages with friends, regardless of shared servers.
  - Send and accept friend requests.
  - View mutual servers of friends.
  - Send files, images, and react to messages using emojis.
- **Notification System**
  - Implement push notifications for new messages and activities.
 
### User Accounts
- **Profile Management**
  - Register new users with HTML client-side validation and database constraints.
  - Update user profile, including avatar, username, email, and password.
  - Manage public and private information, including two-factor authentication.
  - View and manage all orders for admin users.

### Admin Portal
- **Server and User Management**
  - Manage server settings, roles, permissions, and invites.
  - Mute, ban, and manage users within servers.
  - Delete messages and manage server content.
  - Add photos to products and servers using AJAX.
