# URL Shortener Web Application

This web application serves as a URL shortener, allowing users to convert long URLs into shorter, more manageable ones. Similar to services like [https://goo.gl/](https://goo.gl/).

## Features

- **URL Shortening:**
  - Users can enter a long URL in the provided form, and the program generates a short URL using a Timestamp, e.g., `/abc1234`.
  - The short URL is stored along with the corresponding long URL in a database.

- **Redirection:**
  - When a user visits the short URL, the program redirects them to the original long URL.

- **Visit Count:**
  - The program keeps track of how many visits each short URL has received.

- **Statistics Page:**
  - Users can access a statistics page (e.g., `/abc1234/stats`) to view the visit count for a specific short URL.

## Getting Started

To set up and run the project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
