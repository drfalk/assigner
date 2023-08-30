import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 10,
  duration: '5s',
};

export default function () {
  
  const res = http.get('http://localhost:8000');
  console.log(res.body);
  sleep(1);
}
