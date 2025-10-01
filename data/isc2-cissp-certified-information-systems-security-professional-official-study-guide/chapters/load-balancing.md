---
{
  "id": "chapter-147",
  "title": "Load Balancing",
  "order": 147,
  "source": {
    "href": "c12.xhtml",
    "anchor": "head-2-227"
  },
  "est_tokens": 565,
  "slug": "load-balancing",
  "meta": {
    "nav_title": "Load Balancing",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Load Balancing

The purpose of load balancing is to obtain more optimal infrastructure utilization, minimize response time, maximize throughput, reduce overloading, and eliminate bottlenecks. A load balancer is used to spread or distribute network traffic load across several network links or network devices. Although load balancing can be used in a variety of situations, a common implementation is spreading a load across multiple members of a server farm or cluster. Scheduling or load balancing methods are the means by which a load balancer distributes the work, requests, or loads among the devices behind it. A load balancer might use a variety of scheduling techniques to perform load distribution, as described in Table 12.1 .

TABLE 12.1 Common load-balancing scheduling techniques

TABLE 12.1 Common load-balancing scheduling techniques

Load balancing can be either a software service or a hardware appliance. Load balancing can also incorporate many other features, depending on the protocol or application, including caching, TLS offloading, compression, buffering, error checking, filtering, and even firewall and IDS capabilities.

TLS offloading is the process of removing the TLS-based encryption from incoming traffic to relieve a web server of the processing burden of decrypting and/or encrypting traffic sent.

### Virtual IPs and Load Persistence

Virtual IP addresses are sometimes used in load balancing; an IP address is perceived by clients and even assigned to a domain name, but the IP address is not actually assigned to a physical machine. Instead, as communications are received at the IP address, they are distributed in a load-balancing schedule to the actual systems operating on some other set of IP addresses.

Persistence in relation to load balancing is also known as affinity . Persistence is defined as when a session between a client and a member of a load-balanced cluster is established, subsequent communications from the same client will be sent to the same server, thus supporting persistence or consistency of communications.

### Active-Active vs. Active-Passive

An active-active system is a form of load balancing that uses all available pathways or systems during normal operations. In the event of a failure of one or more of the pathways, the remaining active pathways must support the full load that was previously handled by all. This technique is used when the traffic levels or workload during normal operations need to be maximized (i.e., optimizing availability), but reduced capacity will be tolerated during adverse conditions (i.e., reducing availability).

An active-passive system is a form of load balancing that keeps some pathways or systems in an unused dormant state during normal operations. If one of the active elements fails, then a passive element is brought online and takes over the workload for the failed element. This technique is used when the level of throughput or workload needs to be consistent between normal states and adverse conditions (i.e., maintaining availability consistency).
