
# Flask E-Commerce Web Application

## Overview

This project is a simple e-commerce platform built using **Flask**, **SQLite**, and **Jinja2 templates**. It provides functionality for:
- Listing products
- Searching products
- Viewing detailed product information

The application is designed for **learning purposes** and can be extended for real-world use cases.

---

## Data Model

The application uses an **SQLite** database with a single primary table: `products`. Below is the schema for the `products` table:

| **Column Name** | **Data Type** | **Description**                                      |
|------------------|---------------|------------------------------------------------------|
| `ad_no`          | INTEGER       | Primary key. Auto-incremented unique identifier.     |
| `title`          | TEXT          | Title of the product. Cannot be null.               |
| `description`    | TEXT          | A brief description of the product.                 |
| `price`          | REAL          | Price of the product in the local currency.          |
| `city`           | TEXT          | City where the product is available.                |
| `image_url`      | TEXT          | Path or URL to the product's image.                 |
| `category`       | TEXT          | Category of the product (e.g., "Clothing").         |

---

## Assumptions

### Product Data
- All products have a unique `ad_no`.
- Product prices are provided in a consistent currency (e.g., USD, EUR).
- Each product belongs to one category, but the system can be extended to support multiple categories per product.

### Data Validation
- Data validation is assumed to be handled on the front-end or via form validation in Flask forms.

### Database
- The SQLite database is used for simplicity but can be migrated to a relational database like MySQL or PostgreSQL for larger-scale projects.

### Static Files
- All images are stored in the `static/images` folder, and the `image_url` column in the database points to this path.
- CSS styles are included in the `static/css` directory.

### Search Functionality
- The search functionality matches products by `title`, `description`, or `category`.

---

## Features

- **Home Page**:
  - Displays a list of all products categorized by popularity or category.

- **Search Page**:
  - Users can search for products by entering keywords.
  - Results are displayed in a grid layout with product images, descriptions, and prices.

- **Detail Page**:
  - Displays full product details, including:
    - An image
    - Description
    - Price
    - Category
  - Includes breadcrumbs for easy navigation.

- **Database Management**:
  - Products can be added, updated, or deleted from the database.

