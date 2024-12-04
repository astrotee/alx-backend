import { expect } from 'chai';
import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('tests', () => {
  before(function() {
    queue.testMode.enter();
  });

  afterEach(function() {
    queue.testMode.clear();
  });

  after(function() {
    queue.testMode.exit()
  });

  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('test', queue)).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const list = [
      {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
      },
      {
      phoneNumber: '4153518781',
      message: 'This is the code 1235 to verify your account'
      }
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });
})
