const {createPool} = require('mysql');

const pool = createPool({
    host: "localhost",
    user: "root",
    password:"",
    database: "lighten",
    connectionLimit: 5
})

// pool.query(`select * from test`);