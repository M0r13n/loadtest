# Loadtest scenario

This repo holds some loadtesting scenarios for my shop site.

### History
Here I keep track on how the performance evolves over time. The **#concurrent users** is the number of concurrent locust users that can visit the page while the Median response time keeps below 500 ms.


| Date | #concurrent users | comment |
|------|-------------------|---------|
|  02.08.2020    |       350            |     baseline    |
|  03.08.2020    |       900            |     cache main pages (index and /manufacturers)    |
|  03.08.2020    |       1400            |     cache main page via Cloudflare    |