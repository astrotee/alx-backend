export default function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) throw Error('Jobs is not an array');
  for (const job of jobs) {
    const jobCreated = queue.create('push_notification_code_2', job);
    jobCreated
      .on('enqueue', () => {
        console.log(`Notification job created: ${jobCreated.id}`);
      })
      .on('complete', () => {
        console.log(`Notification job ${jobCreated.id} completed`);
      })
      .on('failed', (err) => {
        console.log(`Notification job ${jobCreated.id} failed: ${err}`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${jobCreated.id} ${progress}% complete`);
      });
    jobCreated.save();
  }
}
