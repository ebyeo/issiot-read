'use strict';

var EventHubClient = require('azure-event-hubs').Client;

var connectionString = 'HostName=azureIOThub2017.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=X7Z3y3jEeMzOfaATdL8tf4OkX12G8uZ7S0C2QW79kCM=';

var printError = function (err) {
  console.log(err.message);
};

var printMessage = function (message) {
  console.log('Message received: ');
  console.log(JSON.stringify(message.body));
  console.log('');

  var python = require('child_process').spawn(
     'python',
     // second argument is array of parameters, e.g.:
     ["/opt/iot/change-display.py"]
     );
     var output = "";
     python.stdout.on('data', function(data){ output += data });
     python.on('close', function(code){ 
       if (code !== 0) {  
	console.log("Python - not ok");
	console.log(code);
       } else
	console.log("Python - ok");
     });
};

var client = EventHubClient.fromConnectionString(connectionString);
client.open()
    .then(client.getPartitionIds.bind(client))
    .then(function (partitionIds) {
        return partitionIds.map(function (partitionId) {
            return client.createReceiver('$Default', partitionId, { 'startAfterTime' : Date.now()}).then(function(receiver) {
                console.log('Created partition receiver: ' + partitionId)
                receiver.on('errorReceived', printError);
                receiver.on('message', printMessage);
            });
        });
    })
    .catch(printError);
