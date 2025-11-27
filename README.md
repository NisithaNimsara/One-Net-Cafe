# One Net Cafe — Inventory & Supplier Management

## Overview

One Net Cafe is a Python command-line application to manage inventory and supplier (dealer) details for a small internet café. The tool helps the cafe owner or staff to add, update, delete, and view items; manage supplier records; save and load records; randomly select four dealers; display dealer details by location; and list items provided by a specific dealer.

This README documents installation, usage, storage, testing, and contribution guidelines to get started quickly.

## Features

- Add, update, delete, and view inventory items (name, sku/id, category, quantity, unit price, supplier)
- Add, update, delete, and view suppliers/dealers (name, contact, location)
- Persist data to disk (JSON/CSV or file-based) so records survive restarts
- Randomly select four dealers (useful for promotions or supplier sampling)
- Query dealers by location and view dealer-specific items
- Simple CLI interface suitable for small cafés and local use
