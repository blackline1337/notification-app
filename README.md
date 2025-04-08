# Notification App

A simple API that provides notifications/updates/news.

## Overview

This is a Simple Notification Application.

- Goals
Have a DevOps approach to streamlining the build and deploy of this app using Cloud Services. 



## Application & Deploy Information

### Client Endpoint
- `https://localhost/notifications` - Fetches notifications for clients

### Admin Endpoint
- `https://localhost/{api_path}/add_message` - Interface for adding new text messages/notifications to the database

## Client Implementation

Here's a basic example of how to fetch and display notifications on the client side:

```javascript
async function fetchAndDisplayNotifications() {
    try {
        const response = await fetch('https://localhost/notifications');
        const data = await response.text();
        document.body.innerHTML += data;
    } catch (error) {
        console.error('Error fetching notifications:', error);
    }
}

fetchAndDisplayNotifications();
```