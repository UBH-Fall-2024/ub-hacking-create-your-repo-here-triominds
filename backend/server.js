require("dotenv").config();
const express = require("express");
const cors = require("cors");
const passport = require("passport");
const cookieSession = require("cookie-session");
const passportSetup = require("./passport");
const authRoute = require("./routes/auth");
const mysql = require("mysql");

const app = express();

app.use(
    cookieSession({
        name: "session",
        keys: ["ubbarter"],
        maxAge: 24 * 60 * 60 * 100,
    })
);

app.use(passport.initialize());
app.use(passport.session());

app.use(
    cors({
        origin: "http://localhost:3000",
        methods: "GET, POST, PUT, DELETE",
        credentials: true
    })
);

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password:"",
    database: "test",
    connectionLimit: 5
})
app.use("/auth", authRoute);

app.get('/', (req, res) => {
    return res.json("from backend");
})

app.get('/users', (req, res)=>{
    const sql = "SELECT * from test";
    db.query(sql, (err, data)=>{
        if(err) return res.json(err);
        return res.json(data);
    })
})

const port = process.env.PORT || 8080;
app.listen(port, () => console.log(`Listening on port ${port}...`));

