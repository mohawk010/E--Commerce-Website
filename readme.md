🛒 Ecom Farm - Role Based E‑Commerce Platform
Ecom Farm is a scalable and modern Role-Based E‑Commerce System built using the FARM Stack. It supports both Buyer and Seller modules with secure authentication, clean UI, and production-ready architecture.

🚀 Features
🔑 Role-Based Authentication (Buyer & Seller)
📦 Product Upload, Management & Inventory
🛍️ Product Browsing, Cart & Checkout
📊 Seller Analytics Dashboard
💳 Secure Online Payments
⚡ Optimized UI with Tailwind CSS
🏗️ FARM Stack
Layer	Technology
Frontend	React.js + Tailwind CSS
Backend	FastAPI
Authentication	Role Based Token System
Database	MongoDB
📁 Folder Structure
EcomFarm/
 ├── frontend/      # React + Tailwind
 ├── backend/       # FastAPI APIs 
    ├── config/
    ├── controllers/
    ├── middlwares/
    ├── models/
    ├── routes/
    ├── services/
Enviroment Variables
Frontend
 VITE_APP_RAZORPAY_KEY_ID=
VITE_APP_BACKEND_URI=
Backend
MONGO_URI=
MONGO_DB=ecommerce_farm


JWT_AUTH_SCREATE="!@#$%^&*(@#$%^&*())"

API_KEY_CLOUDINARY=
API_SCREATE_CLOUDINARY=
CLOUD_NAME_CLOUDINARY=


RAZORPAY_KEY_ID=
RAZORPAY_KEY_SCREATE=

FRONTEND_URI=
📦 Installation & Setup
1️) Frontend Setup
cd frontend
npm install
npm run dev
2️) Backend Setup
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
🧑‍🤝‍🧑 Roles in System
👤 Buyer
Browse and purchase products
Add wishlist
🏪 Seller
Upload products & manage inventory
Track orders & analytics
🎨 UI Preview
Clean and modern UI
Styled with Tailwind CSS & React Icons
🧑‍💻 Developer
Designed & Developed by Mohit Verma

If you love this project, ⭐ Star it 