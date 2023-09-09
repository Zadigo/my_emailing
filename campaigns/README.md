# Campaigns

## How it works

A backend server which polls Redis every 5 minutes searches for active campaigns in the Redis database. When a user sets a campaign as active, it's details is stored in the Redis backend.

In a similar, if a campaign is set as inactive, it is also removed from the backend.
