"""

### 🔹 1. **What is an API**

* **API = Application Programming Interface**
* It's a **set of rules** that lets one app interact with another.
* Like a **menu in a restaurant**: you place requests and get responses without knowing the kitchen’s inner details.

---

### 🔹 2. **Why it's called an interface**

* It **defines how two programs talk** to each other.
* You don’t access the app’s internal code — you use its **public-facing interface** (URLs, methods, etc.).

---

### 🔹 3. **What is HTTP**

* **HTTP = HyperText Transfer Protocol**
* It's the **protocol used for communication on the web**.
* It defines how data is **requested (GET)** and **sent (POST)** over the internet.

---

### 🔹 4. **HTTP Protocol Versions**

| Version  | Use Case                           |
| -------- | ---------------------------------- |
| HTTP/1.1 | Still common, used in many servers |
| HTTP/2   | Faster (multiplexed), widely used  |
| HTTP/3   | Ultra-fast, built on QUIC (UDP)    |

* **Real apps**: WordPress (1.1), Amazon/Coursera (2), YouTube/Google (3)

---

### 🔹 5. **What is REST**

* **REST = Representational State Transfer**
* API design pattern that maps **resources** to URLs
* Uses **standard HTTP methods** like `GET`, `POST`, `PUT`, `DELETE`

---

### 🔹 6. **HTTP Methods**

| Method | Action  | Used For         |
| ------ | ------- | ---------------- |
| GET    | Read    | Fetching data    |
| POST   | Create  | Sending new data |
| PUT    | Replace | Full update      |
| PATCH  | Modify  | Partial update   |
| DELETE | Remove  | Delete resource  |

* `POST` is **not idempotent**, others usually are.

---

### 🔹 7. **Status Codes, Headers, and JSON**

#### ✅ Status Codes:

* `200 OK`,
`201 Created`,
`404 Not Found`,
`500 Internal Server Error`, etc.

#### ✅ Headers:

* Key-value pairs sent with requests/responses
* Examples: `Content-Type`, `Authorization`, `User-Agent`

#### ✅ JSON:

* Standard format for request/response bodies
* Easy to parse and used in almost all modern APIs

---
"""