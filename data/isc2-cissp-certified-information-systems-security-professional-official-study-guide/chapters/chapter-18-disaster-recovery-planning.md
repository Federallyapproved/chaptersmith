---
{
  "id": "chapter-259",
  "title": "Chapter 18: Disaster Recovery Planning",
  "order": 259,
  "source": {
    "href": "b01.xhtml",
    "anchor": "head-2-20"
  },
  "est_tokens": 1319,
  "slug": "chapter-18-disaster-recovery-planning",
  "meta": {
    "nav_title": "Chapter 18: Disaster Recovery Planning",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 18: Disaster Recovery Planning

- C. Once a disaster interrupts the business operations, the goal of DRP is to restore regular business activity as quickly as possible. Thus, disaster recovery planning picks up where business continuity planning leaves off. Preventing business interruption is the goal of business continuity, not disaster recovery programs. Although disaster recovery programs are involved in restoring normal activity and minimizing the impact of disasters, this is not their end goal.

- C. The recovery point objective (RPO) specifies the maximum amount of data that may be lost during a disaster and should be used to guide backup strategies. The maximum tolerable downtime (MTD) and recovery time objective (RTO) are related to the duration of an outage, rather than the amount of data lost. The mean time between failures (MTBF) is related to the frequency of failure events.

- D. The lessons learned session captures discoveries made during the disaster recovery process and facilitates continuous improvement. It may identify deficiencies in training and awareness or in the business impact analysis.

- B. Redundant arrays of inexpensive disks (RAID) are a fault-tolerance control that allow an organization's storage service to withstand the loss of one or more individual disks. Load balancing, clustering, and high-availability (HA) pairs are all fault-tolerance services designed for server compute capacity, not storage.

- C. Cloud computing services provide an excellent location for backup storage because they are accessible from any location. The primary data center is a poor choice, since it may be damaged during a disaster. A field office is reasonable, but it is in a specific location and is not as flexible as a cloud-based approach. The IT manager's home is a poor choice—the IT manager may leave the organization or may not have appropriate environmental and physical security controls in place.

- A, B, D. The only incorrect statement here is that business continuity planning picks up where disaster recovery planning leaves off. In fact, the opposite is true: disaster recovery planning picks up where business continuity planning leaves off. The other three statements are all accurate reflections of the role of business continuity planning and disaster recovery planning. Business continuity planning is focused on keeping business functions uninterrupted when a disaster strikes. Organizations can choose whether to develop business continuity planning or disaster recovery planning plans, although it is highly recommended that they do so. Disaster recovery planning guides an organization through recovery of normal operations at the primary facility.

- B. The term 100-year flood plain is used to describe an area where flooding is expected once every 100 years. It is, however, more mathematically correct to say that this label indicates a 1 percent probability of flooding in any given year.

- D. When you use remote mirroring, an exact copy of the database is maintained at an alternative location. You keep the remote copy up to date by executing all transactions on both the primary and remote sites at the same time. Electronic vaulting follows a similar process of storing all data at the remote location, but it does not do so in real time. Transaction logging and remote journaling options send logs, rather than full data replicas, to the remote location.

- C. All of these are good practices that could help improve the quality of service that Bryn provides from her website. Installing dual power supplies or deploying RAID arrays could reduce the likelihood of a server failure, but these measures only protect against a single risk each. Deploying multiple servers behind a load balancer is the best option because it protects against any type of risk that would cause a server failure. Backups are an important control for recovering operations after a disaster and different backup strategies could indeed alter the RTO, but it is even better if Bryn can design a web architecture that lowers the risk of the outage occurring in the first place.

- B. During the business impact analysis phase, you must identify the business priorities of your organization to assist with the allocation of BCP resources. You can use this same information to drive the disaster recovery planning business unit prioritization.

- C. The cold site contains none of the equipment necessary to restore operations. All of the equipment must be brought in and configured and data must be restored to it before operations can commence. This process often takes weeks, but cold sites also have the lowest cost to implement. Hot sites, warm sites, and mobile sites all have quicker recovery times.

- C. Uninterruptible power supplies (UPSs) provide a battery-backed source of power that is capable of preserving operations in the event of brief power outages. Generators take a significant amount of time to start and are more suitable for longer-term outages. Dual power supplies protect against power supply failures and not power outages. Redundant network links are a network continuity control and do not provide power.

- D. Warm sites and hot sites both contain workstations, servers, and the communications circuits necessary to achieve operational status. The main difference between the two alternatives is the fact that hot sites contain near-real-time copies of the operational data and warm sites require the restoration of data from backup.

- D. The parallel test involves relocating personnel to the alternate recovery site and implementing site activation procedures. Checklist tests, structured walk-throughs, and simulations are all test types that do not involve actually activating the alternate site.

- A. The executive summary provides a high-level view of the entire organization's disaster recovery efforts. This document is useful for the managers and leaders of the firm as well as public relations personnel who need a nontechnical perspective on this complex effort.

- D. Software escrow agreements place the application source code in the hands of an independent third party, thus providing firms with a “safety net” in the event a developer goes out of business or fails to honor the terms of a service agreement.

- A. Differential backups involve always storing copies of all files modified since the most recent full backup, regardless of any incremental or differential backups created during the intervening time period.

- B. People should always be your highest priority in business continuity planning. As life safety systems, fire suppression systems should always receive high prioritization.

- A. Any backup strategy must include full backups at some point in the process. If a combination of full and differential backups is used, a maximum of two backups must be restored. If a combination of full and incremental backups is chosen, the number of required restorations may be large.

- B. Parallel tests involve moving personnel to the recovery site and gearing up operations, but responsibility for conducting day-to-day operations of the business remains at the primary operations center.
