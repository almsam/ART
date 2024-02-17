# What our project is:
Discord clone

# What our project offers:
Our project will offer a messaging system similar to Discord where users can join servers and send and receive text messages both on their servers and between individual users regardless if they share the same server. Server members will be notified when new messages are sent to them directly or posted to their servers.

# Basic Functions:
- Login
- Servers with messaging channels
- Direct Messaging and friend system
- Database system to receive information and send information to users

# User Requirements:
- Link to "sign-up" page if no login exists
- Be able to log into user accounts
- Login page
- Be able to write and send messages
- Be able to join servers and send messages within those servers
- Ability to send and accept friend requests
- Ability to send files and images
- Ability to check mutual servers of friends
- Ability to add a user description
- React to messages using emojis
- Create and manage servers, including the users within servers
- Put an image for a server icon
- Ability to search for servers, channels, and within chat history.
- Ability to generate invite link
- Ability to create & delete channels (if admin permissions exist)
- Changing personal info
  - Public info
			Profile pictures
			Usernames
			Public roles
		Private info
			Name
			Email
			Two-Factor Authentication
	Ability to manage the server (if admin permissions exist)
		Mute people
		Ban people
		Delete messages

# Functional Requirements:
	Login/Registration Page: Secure entry points for user authentication and registration, including options for resetting passwords.
	Display a list of servers the user is part of, with options to join or create new servers.
	Show channels of the selected server, categorized by text and voice channels, including functionality to create, edit, or delete channels (based on user permissions).
	Text channel user interface for viewing, sending, and receiving messages. Features include message formatting, emoji support, image/video/file attachments, and links.
	User interface for voice/video communication, including mute, deafening, user volume control, and screen sharing options. (Optional due to difficulty)
	Notification System: Implement push notifications for desktop and mobile devices to alert users of new messages and activities.
	Interface for adjusting user profile settings, including avatar, username, email, password, and notification preferences.
	User Management: make sure each user's private data is hidden from other users & public data is easily accessible & readable.
	For server owners or admins: interfaces for managing server settings, roles, permissions, and invites.
	Interface for private messaging between users, including group direct messages.
	Friends: option to send a friend request to another user, accept a friend request from a user, and view mutual friends and servers of friends.
	Display the online/offline status of friends, with options to add, remove, or block users.
	Server Creation and Management: Allow users to create and manage servers, including settings for privacy, roles, and permissions.
	Channel Management: Handle the creation, editing, and deletion of text and voice channels within servers.
	Implement role-based access control for different levels of functionality within servers and channels.

# Non-Functional Requirements:
	Must be developed using Java.
	Implement a database to ensure each user can upload & download the message history for each chat:
		Database management must use SQL.
		Stores server information
		Stores messages, files, images, and videos within servers and direct messages
		Stores user information
			User name
			User ID
			Servers user is in
			If user is an admin
			User's friend list (list of user IDs)
		Stores textbox and reply thread
		Stores moderator and other role assignments
		Database Management: Efficiently store and query data related to users, servers, channels, and messages.
	Updates (messages, profile updates, server updates etc.) must be made in real time with as little lag as possible (preferably within one second).
	Load Balancing: Efficiently distribute traffic across servers to ensure smooth performance under high load.
	Data Management and Security: make sure to implement end to end encryption & two-factor authentication.
	API Security: Secure API endpoints against common vulnerabilities and unauthorized access.
	Scalability and Performance: Ensure that the system can easily implement data warehousing techniques to function at large scales.
	Caching: Implement caching strategies for frequently accessed data to reduce database load and improve response times.
	Real-time Data Synchronization: Use WebSockets or similar technology for real-time updates across client devices.
	Must be compatible with major operating systems such as Microsoft Windows.
