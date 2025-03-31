# Notification App

A simple API that provides notifications/updates/news.

## Overview

This is a basic notification application that allows administrators to send notifications and clients to receive them.

## Server Endpoints

### Client Endpoint
- `https://localhost/myapi/notifications` - Fetches notifications for clients

### Admin Endpoint
- `https://localhost/myapi/add-notification` - Interface for adding new text messages

## Client Implementation

Here's a basic example of how to fetch and display notifications on the client side:

```javascript
async function fetchAndDisplayNotifications() {
    try {
        const response = await fetch('https://localhost/myapi/notifications');
        const data = await response.text();
        document.body.innerHTML += data;
    } catch (error) {
        console.error('Error fetching notifications:', error);
    }
}

fetchAndDisplayNotifications();
```