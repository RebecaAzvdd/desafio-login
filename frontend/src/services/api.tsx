import axios from 'axios';

const apiUsers = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/users/',
});

export default apiUsers;