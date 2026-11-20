# Alexander Hossak

**Kubernetes platform & security engineer.** I build Kubernetes platforms that are secure by default, reproducible from code, and boring to operate.

[![Kubestronaut](https://img.shields.io/badge/CNCF-Kubestronaut-326CE5?style=flat-square&logo=kubernetes&logoColor=white)](https://www.credly.com/users/alexander-hossak)

<p>
  <a href="https://www.credly.com/badges/2cc144f0-6d46-423c-97ad-705a55f5149c/public_url"><img src="https://images.credly.com/size/110x110/images/8b8ed108-e77d-4396-ac59-2504583b9d54/cka_from_cncfsite__281_29.png" width="90" alt="CKA" /></a>
  <a href="https://www.credly.com/badges/30c458bc-6b55-40bc-ac16-dd406b9ecead/public_url"><img src="https://images.credly.com/size/110x110/images/cc8adc83-1dc6-4d57-8e20-22171247e052/blob" width="90" alt="CKAD" /></a>
  <a href="https://www.credly.com/badges/58d1a603-f08c-42eb-827f-a068c59361d0/public_url"><img src="https://images.credly.com/size/110x110/images/9945dfcb-1cca-4529-85e6-db1be3782210/kubernetes-security-specialist-logo2.png" width="90" alt="CKS" /></a>
  <a href="https://www.credly.com/badges/bc30db5f-c6b3-4474-a48c-e5587df6d78e/public_url"><img src="https://images.credly.com/size/110x110/images/67dd8a95-8876-4051-9cb9-3d97c204f85a/image.png" width="90" alt="KCSA" /></a>
  <a href="https://www.credly.com/badges/a04e166f-9d2c-4a08-9128-ce2662ef53ab/public_url"><img src="https://images.credly.com/size/110x110/images/f28f1d88-428a-47f6-95b5-7da1dd6c1000/KCNA_badge.png" width="90" alt="KCNA" /></a>
</p>

---

### What I work on

- **Kubernetes platforms.** Highly available, fully declarative clusters on Talos Linux: bare metal, immutable nodes, no SSH, API access over mTLS only.
- **Platform security.** Default-deny networking with Cilium up to layer 7, Kyverno admission policies, Falco runtime detection, signed images, Trivy in CI, regular checks against the CIS Kubernetes Benchmark.
- **Reliability.** Monitoring and alerting with Prometheus, Grafana and Loki, exercised disaster-recovery restores, postmortems, and 24/7 on-call for production systems.
- **AI infrastructure.** Self-hosted LLM inference, knowledge-graph memory servers for coding agents over MCP, and LLM routing through a central gateway.

### Selected work

- Designed and ran the migration of a healthcare IoT company's container platform to a highly available Talos Linux cluster with Cilium, Kyverno, Falco and Rook-Ceph.
- Modernised the company's entire production Linux infrastructure: every server and LXC container moved off end-of-life Ubuntu 16.04 to Rocky Linux 9 and Docker Compose, fully automated with Ansible.
- Moved a multi-terabyte production PostgreSQL 10 database to a highly available PostgreSQL 16 cluster (Patroni, etcd).
- Introduced secret management: hard-coded credentials removed from the code repositories, repositories sanitised, exposed passwords and keys rotated.
- Kept more than 7,500 IoT gateways running in hospitals worldwide.

### Currently building

- **cf-ai-edge-demo**: a retrieval-augmented question-answering API on Cloudflare's edge (Workers AI, AI Gateway, Vectorize), protected by Cloudflare Access and a WAF rate limit, with measured latency and cost per request.
- **Homelab**: an 8-node Raspberry Pi 4B Kubernetes cluster and a dedicated Proxmox server as a remote lab.

### Stack

**Kubernetes:** Talos Linux · Cilium · Kyverno · Falco · Rook-Ceph · Argo CD · K3s · GKE<br>
**Automation:** Ansible · Terraform · Packer · GitLab CI/CD · GitHub Actions<br>
**Observability:** Prometheus · Grafana · Loki · Zabbix<br>
**Systems:** Linux · PostgreSQL · WireGuard · Active Directory · Keycloak<br>
**Languages:** Python · Go · Bash

### Contact

[LinkedIn](https://www.linkedin.com/in/alexander-hossak) · [Credly](https://www.credly.com/users/alexander-hossak) · [certdirectory](https://certdirectory.io/profile/alexander-hossak)
