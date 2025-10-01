---
{
  "id": "chapter-107",
  "title": "Containerization",
  "order": 107,
  "source": {
    "href": "c09.xhtml",
    "anchor": "head-2-176"
  },
  "est_tokens": 348,
  "slug": "containerization",
  "meta": {
    "nav_title": "Containerization",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Containerization

Containerization is the next stage in the evolution of the virtualization trend for both internally hosted systems and cloud providers and services. A virtual machine–based system uses a hypervisor installed onto the bare metal of the host server and then operates a full guest OS within each virtual machine, and each virtual machine often supports only a single primary application. This is a resource-wasteful design and reveals its origins as separate physical machines.

Containerization or OS-virtualization is based on the concept of eliminating the duplication of OS elements in a virtual machine. Instead, each application is placed into a container that includes only the actual resources needed to support the enclosed application, and the common or shared OS elements are then part of the hypervisor. Some deployments claim to eliminate the hypervisor altogether and replace it with a collection of common binaries and libraries for the containers to call upon when needed. Containerization is able to provide 10 to 100 times more application density per physical server than that provided by traditional hypervisor virtualization solutions.

Application cells or application containers ( Figure 9.4 ) are used to virtualize software so that they can be ported to almost any OS.

FIGURE 9.4 Application containers versus a hypervisor

FIGURE 9.4 Application containers versus a hypervisor

There are many different technological solutions that are grouped into the concept of containerization. Some refer to the application instances as containers , zones , cells , virtual private servers , partitions , virtual environments , virtual kernels , or jails . Some containerization solutions allow for multiple concurrent applications within a single container, whereas others are limited to one per container. Many containerization solutions allow for customization of how much interaction applications in separate containers is allowed.
