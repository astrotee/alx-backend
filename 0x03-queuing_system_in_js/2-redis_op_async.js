import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ' + err);
});

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  promisify(client.GET).bind(client)(schoolName).then((value) => {
    console.log(value);
  });
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
