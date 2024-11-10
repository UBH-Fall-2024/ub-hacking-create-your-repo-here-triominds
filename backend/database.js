const {createPool} = require('mysql');

const pool = createPool({
    host: "localhost",
    user: "root",
    password:"",
    database: "test",
    connectionLimit: 5
})

pool.query(`select * from test`);