# Changelog

All notable changes to this project will be documented in this file.

## 1.0.0 (2025-11-26)

### Features

* add etcd storage ([d68c47a](https://github.com/mariusbertram/ansible-vault/commit/d68c47af0aef1dcd297f7a01be155717cb164bb9))
* Add raft backed support ([2334138](https://github.com/mariusbertram/ansible-vault/commit/2334138e10560aa81e6480ff43364e19d034463f))
* add support for AlmaLinux ([04caf06](https://github.com/mariusbertram/ansible-vault/commit/04caf067e231a5efbd55667df6f730fc221b1911))
* add support for AmazonLinux ([15a6774](https://github.com/mariusbertram/ansible-vault/commit/15a677441f568d5d2d148dc7cc20f83b6c0192f6))
* add support for debian 12 ([7720ead](https://github.com/mariusbertram/ansible-vault/commit/7720eadc3b38402d1e86f4da22e7d6eb2c634caf))
* add support for EL9 distros ([b7e27aa](https://github.com/mariusbertram/ansible-vault/commit/b7e27aac402c950abf4c580e1e42b56cf699798f))
* add support for installing vault plugins ([37caf93](https://github.com/mariusbertram/ansible-vault/commit/37caf93cf06e7e503191baaf5ea93681addcbde8))
* add support for the current versions of debian/ubuntu ([438493a](https://github.com/mariusbertram/ansible-vault/commit/438493aac7b5ae4e911d1d9fe13a40897bff4c42))
* add vault log to file with vault_enable_log ([a7b7646](https://github.com/mariusbertram/ansible-vault/commit/a7b76466e1c2949c28f2db0d935d8a2e8a82d419))
* **ci:** auto discover molecule scenarios ([ee2d820](https://github.com/mariusbertram/ansible-vault/commit/ee2d8202bc79cfb5d7c1d480056bca6a42bf5b6f))
* **GHA:** add commitlint and semrel ([#362](https://github.com/mariusbertram/ansible-vault/issues/362)) ([d5bae97](https://github.com/mariusbertram/ansible-vault/commit/d5bae97c79a783b2b7044d3b166dd2f0495666e9))
* **plugins:** support using token from vault cli token helper ([4c61eb3](https://github.com/mariusbertram/ansible-vault/commit/4c61eb320cd428476028778523bf3eec08e2e1c2))
* **seal:** add support for ocikms ([eea06b9](https://github.com/mariusbertram/ansible-vault/commit/eea06b9626f2764204bc3b3b265c04b0e7a6da40))
* support Fedora ([1def881](https://github.com/mariusbertram/ansible-vault/commit/1def881da27a90150a0bf2f9b54433b26823dbed))
* **testing:** add molecule scenarios for all of the platforms that the role supports ([38b2d40](https://github.com/mariusbertram/ansible-vault/commit/38b2d40afc167276b2e6375be28de7de607c81b6))

### Bug Fixes

* adopted molecule to ansible v2.19, fixed OS names ([820131c](https://github.com/mariusbertram/ansible-vault/commit/820131c5a0abb930a8155421f194ca0d8aa93e12))
* amazonlinux 2022 repo ([ca78fd0](https://github.com/mariusbertram/ansible-vault/commit/ca78fd06d5a9a546470ff9a678f534a290f97dd3))
* amazonlinux repo ([4dc2170](https://github.com/mariusbertram/ansible-vault/commit/4dc2170526f79f585bd8755c7b59d539950a8fa8))
* applying PR[#302](https://github.com/mariusbertram/ansible-vault/issues/302) comments ([d7389f5](https://github.com/mariusbertram/ansible-vault/commit/d7389f575d778ed59597a21735db9774290393cb))
* **ci:** failing legacy platforms and delegation issues. ([#321](https://github.com/mariusbertram/ansible-vault/issues/321)) ([6a18b80](https://github.com/mariusbertram/ansible-vault/commit/6a18b8043cc7b64d3f9a9c095f3e473e615c9354))
* **ci:** ignore examples dir in ansible lint ([#327](https://github.com/mariusbertram/ansible-vault/issues/327)) ([0f9d34c](https://github.com/mariusbertram/ansible-vault/commit/0f9d34ce4eaf7ed82c78b103f7f0aca4621b9d40))
* correct vault group in goss tests ([446859b](https://github.com/mariusbertram/ansible-vault/commit/446859ba8d4e42e0e86e2b07b178654696a87deb))
* distro versions in readme ([c7bfd0e](https://github.com/mariusbertram/ansible-vault/commit/c7bfd0ecf2721842e9f5c34272bab5582f49cee1))
* indentation of vault config file ([7e8aa3f](https://github.com/mariusbertram/ansible-vault/commit/7e8aa3fa58e272bcefd5c9dc3d64cc15d02abc12))
* jinja2 linting ([0cac363](https://github.com/mariusbertram/ansible-vault/commit/0cac3639dfe84a3db0aa8a7c02b152847c0c1dba))
* **lint:** Templated files should use template instead of copy ([aa43735](https://github.com/mariusbertram/ansible-vault/commit/aa437354db200459e5adbf92ddf6f1ce4963f17c))
* only set client_ca_file for tcp listener when defined ([a7a314c](https://github.com/mariusbertram/ansible-vault/commit/a7a314c992f72e04d3847a6a11326ca6dfd36a76))
* **pkcs11:** jinja whitespace ([b872b09](https://github.com/mariusbertram/ansible-vault/commit/b872b09ebc754bc13515e5832225540b0cf47df6))
* remove debian 12 since it's a prerelease ([c3cd9e7](https://github.com/mariusbertram/ansible-vault/commit/c3cd9e72da283a30dcf8a2c885c83a8e177d0459))
* remove vault_tls_prefer_server_cipher_suites ([fa5a7e6](https://github.com/mariusbertram/ansible-vault/commit/fa5a7e613bc2f11b59e65b97ce55c4db429f0b2a))
* remove vault_tls_prefer_server_cipher_suites defaults ([c7dcf03](https://github.com/mariusbertram/ansible-vault/commit/c7dcf0312318e68fdf6ef44ecf7717551b777509))
* replace deprecated include with include_tasks ([6e3e032](https://github.com/mariusbertram/ansible-vault/commit/6e3e032a1271744712249530cbf10391e3828d47))
* resolve deprecation warnings and move become flag to required resources ([c404967](https://github.com/mariusbertram/ansible-vault/commit/c404967af422cc63a946c35992efcf617d4bd1f1))
* risky-file-permissions ([3729dbf](https://github.com/mariusbertram/ansible-vault/commit/3729dbfcd584f9fb9fcbfea935da33efa1f059e0))
* **semrel:** fix branch ([#363](https://github.com/mariusbertram/ansible-vault/issues/363)) ([ec91b6c](https://github.com/mariusbertram/ansible-vault/commit/ec91b6ca1bc61444be0cf8b916ba4ebce6608962))
* **semrel:** fix branch ([#364](https://github.com/mariusbertram/ansible-vault/issues/364)) ([2c87dd4](https://github.com/mariusbertram/ansible-vault/commit/2c87dd4a372defffa77670dab6ce00cbd3ae219d))
* set vault_os_packages for RedHat ([293f7ad](https://github.com/mariusbertram/ansible-vault/commit/293f7ade4bff79b9d9eeda56c7edd0837ed49d17))
* shameless self plug ([f2be6f9](https://github.com/mariusbertram/ansible-vault/commit/f2be6f990719820b92bca3f0571cd702bbb35382))
* **smerel:** bump changelog to 8.0.0 ([#365](https://github.com/mariusbertram/ansible-vault/issues/365)) ([7e2fded](https://github.com/mariusbertram/ansible-vault/commit/7e2fdeddec3405756aae10f1dedcace4ba94779b))
* systemd unit option `ConditionFileExists` ([12d294d](https://github.com/mariusbertram/ansible-vault/commit/12d294defd908b62c0d46f058db6768fe74fde99))
* tasks that check if vault is installed shouldn't be handlers ([60c7478](https://github.com/mariusbertram/ansible-vault/commit/60c747887704d0a8e4a4983462623f09e162fc72))
* template can't write content to file ([8940571](https://github.com/mariusbertram/ansible-vault/commit/894057188efa1510e42d7d5d9b68e785872278d6))
* temporarily disable overly strict lint rule ([5695e34](https://github.com/mariusbertram/ansible-vault/commit/5695e34f96312341b791de4b32834ac189897ad0))
* use AmbientCapabilities only when systemd version is >= 230 ([6c15be4](https://github.com/mariusbertram/ansible-vault/commit/6c15be46c94a6b1be02cd91ef83a42d256aa400d)), closes [/github.com/systemd/systemd/blob/8f968c7321be09e7a41b29a0d5d2d2c13ee7ded1/NEWS#L1357](https://github.com/mariusbertram//github.com/systemd/systemd/blob/8f968c7321be09e7a41b29a0d5d2d2c13ee7ded1/NEWS/issues/L1357) [brianshumate/ansible-vault#67](https://github.com/brianshumate/ansible-vault/issues/67)

### Reverts

* Revert "Replace server variable with inventory_hostname in raft configuration" ([b798fdd](https://github.com/mariusbertram/ansible-vault/commit/b798fddff83d953f81b40b4669f5a545af3eb722))

## NEXT

- Add support for proxy configuration
- Add support for system certificates with `vault_tls_certs_path` and `vault_tls_private_path`

## v2.5.9
- Add ability to install Vault Enterprise via HashiCorp Repo
- Removed check of non-existent variable "vault_install_remote_repo" in tasks/main.yml
- Bumped Vault version to v1.18.2
- Revamped Readme

## v2.5.8
- Add vault_unauthenticated_metrics_access to listener

## v2.5.7
- Added support for useful options when running Vault behind a load balancer

## v2.5.6
- Fix systemd forking process bug that prevents to stop/restart vault properly
- Use exec to replace the calling process which effectively nullify the forkin problem

## v2.5.5
- become_user vault_user when modifying files in vault_home

## v2.5.4
- New installation instructions

## v2.5.3
- Add Prometheus telemetry support (thanks @bbayszczak)
- Add tag check_vault to to Vault status debug task (thanks @NorthFuture)
- Fixed indentation of vault config file (thanks @rasta-rocket)
- Add RHEL 8 support (thanks @kwevers)

## v2.5.2

- Vault v1.3.2
- Update documentation

## v2.5.1

- Vault v1.3.1
- Add MySQL storage (thanks @ericsysmin)
- Update status task (thanks @ericsysmin)
- Add group creation task (thanks @karras)
- Update documentation (thanks @ilpianista)
- Update documentation

## v2.5.0

- Vault v1.3.1
- Update documentation

## v2.4.0

- Vault v1.2.4
- Restart after binary change (thanks @bbaassssiiee)
- Use command for vault version in main tasks (thanks @bbaassssiiee)
- Update API status check (thanks @bbaassssiiee)
- Support Fedora (thanks @rbjorklin)
- Update CONTRIBUTORS
- Update documentation

## v2.3.4

- Vault v1.2.3
- Fix s3 backend configuration and template (thanks @ebostijancic)
- Update documentation

## v2.3.3

- Vault v1.2.2
- Update documentation

## v2.3.2

- Fix Vault installation check (thanks @jpiron)
- Update documentation

## v2.3.0

- Vault v1.2.0
- Update documentation

## v2.2.3

- Vault v1.1.5
- Add DynamoDB storage backend (thanks @chris-dudley)
- Update CONTRIBUTORS
- Update documentation

## v2.2.2

- Vault v1.1.4
- Add support for backend tls configuration (thanks @rhenwood3995)
- Fix template line break (thanks @fhemberger)
- ansible_default_ipv4 interface used as default (thanks @fhemberger)
- Update vault_home (thanks @zeridon)
- Add s3 storage backend template (thanks @dvmonroe)
- Update documentation (thanks @dvmonroe)
- Update CONTRIBUTORS

## v2.2.1

- Resolve some task argument issues
- Clean up line length a bit
- Use Filesystem Storage Backend in Vagrant example playbook
- Update Vagrantfile
- Update documentation

## v2.2.0

- Clean up task items
- Fixup Get installed Vault version for multiline/quotes
- Update vault_home value (thanks @xeivieni)
- Add plugin_dir configuration (thanks @vmwiz)
- Fix: Force `/bin/bash` on Get Vault package checksum (local) (thanks @fleu42)

## v2.1.9

- Vault version 1.1.2
- Feature: add etcd storage (thanks @cordula-grau)
- Fix: Resolve deprecation warnings (thanks @cordula-grau)
- Fix: Move become flag to required resources (thanks @cordula-grau)
- Reposition some main variables
- Remove `vault_tls_cipher_suites` values/fall back to Vault defaults
- Remove unimplemented `vault_syslog_enable`
- Rename `vault_listener_template` to `vault_main_configuration_template`
  - Rename corresponding template file to `vault_main_configuration.hcl.j2`
- Update documentation

## v2.1.8

- Vault version 1.1.1
- Allow sealed state for standalone instance (thanks @kwevers)
- Revert long line syntax change in main tasks (thanks @kwevers)
- Ensure systemd is reloaded on unit changes (thanks @kwevers)
- Add vault_bin_path to the PATH (thanks @kwevers)
- Update documentation

## v2.1.7

- Minimum Ansible version to 2.7
- Support install on Debian Testing (thanks @gfeun)
- Update for E206 [lint]
  - tasks/tls
- Update for E201 [lint]
  - tasks/main
- Update for E504 [lint]
  - tasks/install
  - tasks/install_enterprise
- Use bool filter in template conditionals
- Consistent seal template filenames
  - awskms seal (now named vault_seal_awskms.j2)
  - azurekeyvault seal (now named `vault_seal_azurekeyvault.j2`)
  - gcpkms seal template (now named `vault_seal_gcpkms.j2`)
  - pkcs11 seal template (now named `vault_seal_pkcs11.j2`)
- Consistent service template names
  - BSD style init script (now named `vault_service_bsd_init.j2`)
  - Debian style init script (now named `vault_service_debian_init.j2`)
  - systemd unit (now named `vault_service_systemd.j2`)

## v2.1.6

- Resolve environment additions/create .bashrc (thanks @gfeun)
- Update documentation
- Update license
- Update variables

## v2.1.5

- Vault v1.1.0
- Add additional health responses to API reachability check (thanks @enqack)
- VAULT_ADDR and VAULT_CACERT export in ~/.bashrc (thanks @planetrobbie)
- Update documentation

## v2.1.4

- Replace Azure Key Vault variables to resolve #85
- Tidy and reorganize main variables

## v2.1.3

- Vault v1.0.3
- Skip certificate copy if desired (thanks @Fuochi-YNAP)
- Skip health check if desired (thanks @Fuochi-YNAP)
- Add Azure Key Auto Unseal configuration (thanks @nehrman)

## v2.1.2

- Vault v1.0.2
- Update documentation

## v2.1.1

- Vault v1.0.1
- AWS KMS seal support (thanks @jeffWelling)
- Enable web UI by default
- Update documentation

## v2.1.0

- Vault v1.0.0
- GCPKMS seal support (thanks @planetrobbie)
- Update documentation

## v2.0.9

- Correct systemd unit (thanks @jpiron)
- Add initial telemetry support (thanks @jeffWelling)
- Vagrant box memory increased to 2048MB
- Update documentation

## v2.0.8

- Vault v0.11.5
- Conditional capabilites based on systemd version (thanks @bdossantos)
- Update documentation

## v2.0.7

- Vault v0.11.3
- Templates in main tasks as variables (thanks @nathkn)
- systemd unit updates (thanks @bdossantos)
- Update documentation

## v2.0.5

- Vault v0.11.2
- Update systemd unit
- Update Consul storage backend template (thanks @jpiron)
- Configuration updates (thanks @jpiron)
- Add client cert validation options to listener configuration (thanks @nathkn)

## v2.0.4

- Vault v0.11.1
- Update tasks/normalize conditionals
- Update TLS variable names to match documentation
- Conditional mlock capability (thanks @jpiron)
- Streamline installation tasks (thanks @jpiron)
- Update documentation

## v2.0.3

- Vault version 0.10.4
- Debian 9 support
- Update support for enterprise versions (thanks @drewmullen)
- Log rotation updates (thanks @drewmullen)
- Update systemd unit file
- Update documentation

## v2.0.2

- Option to disable cert validation during API reachability (thanks @eripa)
- Update systemd unit to address #41

## v2.0.1

- Vault v0.10.1
- Simplify cleanup task in remote install
- enable_ui option (thanks @aarnaud)
- Enhance API reachable check (thanks @aarnaud)
- Add support for HTTPS in Consul backend (thanks @eripa)
- Add support for HTTP 429 when vault_cluster_disable false (thanks @eripa)
- Update CONTRIBUTORS
- Update documentation

## v2.0.0

- Vault version 0.10.0
- Update documentation
- Update Vagrant documentation

## v1.8.0

- Vault version 0.9.6
- Update is Vault API reachable task (thanks @rarguelloF)
- File storage backend (thanks @aarnaud)
- Update example versions
- Update license date
- Update CONTRIBUTORS
- Update documentation

## v1.7.9

- Vault version 0.9.5
- Remove abs check on cluster_address in Consul backend to fix #33
- Update documentation

## v1.7.8

- Vault version 0.9.4
- TLS already on remote source option (thanks @calebtonn)
- Update documentation

## v1.7.7

- Vault version 0.9.3
- Update documentation

## v1.7.6

- Vault version 0.9.2
- Update documentation

## v1.7.5

- Vault version 0.9.1
- Update documentation

## v1.7.4

- Vault version 0.9.0
- Use HTTPS when TLS is enabled (thanks @tbartelmess)
- Add Consul ACL token option to configuration (thanks @Lavoaster)
- Update CONTRIBUTORS.md

## v1.7.3

- Vault v0.8.3
- Updated supporting software versions
- Add vault_max_lease_ttl and vault_default_lease_ttl (thanks @bilke)

## v1.7.2

- Vault v0.8.2
- Update README (thanks @Gerrrr)
- Update init scripts (thanks @Gerrrr)
- Add vault_consul_service in consul storage template (thanks @Gerrrr)
- Update CONTRIBUTORS.md (thanks @groggemans)

## v1.7.1

- Vault v0.8.1

## v1.7.0

- Vault v0.8.0
- Fix Missing Defaults for TLS (thanks @marc-sensenich)
- Add missing redirect_addr in HA consul config (thanks @groggemans)
- Update CONTRIBUTORS

## v1.6.8

- Enterprise task changes
- Add `vault_install_remotely` docs
- Add `vault_remote_tmp` variable and use it
- Rename `cluster_nodes` label to `vault_instances`

## v1.6.7

- Vault version 0.7.3
- Update documentation

## v1.6.6

- Explicit Vault address (0.0.0.0 is not good for HA mode)
- Update listener template (thanks @groggemans)
- Add vault_consul_path in consul storage template (thanks @groggemans)
- Fix BSD init task and remove unused grouping (thanks @groggemans)
- Update defaults order (thanks @groggemans)
- Make vault user management configurable (thanks @groggemans)
- Add UI switch (enterprise) and fix tls_disable (thanks @groggemans)
- Remove no longer used 'primary_node' variable (thanks @groggemans)
- Add missing README entries (thanks @groggemans)

## v1.6.5

- Correct main tasks

## v1.6.4

- Enable Vault Enterprise tasks
- Remove `redirect_addr` in favor of request forwarding
- Make `vault_log_level` environment variable override
- Update documentation

## v1.6.3

- Correct Vault Enterprise variables to address #18

## v1.6.2

- Vault version 0.7.2
- Minor play updates
- Move asserts to asserts.yml file (thanks @groggemans)

## v1.6.1

- Vault version 0.7.1
- Further task cleanup

## v1.6.0

- Add initial Vault Enterprise variables
- Add initial Vault Enterprise installation tasks
- Update when statements to avoid warnings about template delimiters
- Update documentation

## v1.5.7

- Add TLS directory task to TLS tasks (thanks @cwill747)
- Update CONTRIBUTORS
- Update CONTRIBUTING
- Update documentation

## v1.5.6

- Update remote tasks

## v1.5.5

- Back to local_action for the download and unzip tasks
- Already using grep, so let's just awk for the SHA and then register it
- Add remote install capability (thanks @bilke)

## v1.5.4

- Update documentation on new netaddr dependency _sweat_

## v1.5.3

- Revert local_action tasks
  - They are broken in every case I tested, and connection local is perfectly
    valid for running things on the local host :|

## v1.5.2

- Switch to local actions (addresses #13)

## v1.5.1

- Fixed vault_tls_cert_file and vault_tls_key_file vars

## v1.5.0

- Add initial multi-architecture and OS support
- Add FreeBSD support
- Update documentation

## v1.4.2

- All quoting issues sorted

## v1.4.1

- Fix finicky var quoting issue

## v1.4.0

- Updated many variables with environment variable overrides
- Add `vault_tls_config_path` variable with reasonable default value
- Set currently/reasonably secure `vault_tls_cipher_suites` defaults
- Update listener template to finally close #3
- Improve cleanup task
- Update versions
- Update documentation
- Update ignores

## v1.3.12

- Made VAULT_IFACE environment variable override

## v1.3.11

- Update init scripts

## v1.3.10

- Fix other modes / types ノ( ゜-゜ノ)

## v1.3.9

- Fix quote removal/type finagling YAML sadness (thanks @arledesma)

## v1.3.8

- Move TLS bits to separate task
- Short circuit TLS bits as bad things™ were happening due to the empty
  cert and key values during the Vault SSL Certificate and Key copy ops
  (probably an Ansible bug, copying entire contents of files to vault etc dir)
  No bueno

## v1.3.7

- Replace lost double quote (thanks @arledesma)
- Add explicit vault user permissions to config (thanks @arledesma)
- Remove duplicate cluster_address var
- Update README / consistent variable style / more links to docs

## v1.3.6

- Handle cluster_addre differently
- Cleanup tasks
- Consistent variable style
- Cleanup meta

## v1.3.5

- Remove explicit cluster_addr and let Vault default the value for now

## v1.3.4

- Use vault_port+1 in cluster_addr for HA vault (thanks @arledesma)
- Update CHANGELOG
- Update Vagrant README

## v1.3.3

- Update systemd unit file

## v1.3.2

- Make vault user a system account

## v1.3.1

- Vault 0.7.0
- Initial TLS bits (thanks @arledesma)
- Fix logging options (thanks @arledesma)
- Update documentation

## v1.3.1

- Add support for version specification via VAULT_VERSION environment variable
- Renamed backend configuration template
- Renamed main template to be inline with configuration section naming
- Fix broken unit file

## v1.2.10

- Use all defined variables (thanks @arledesma)
- Make redirect_address more specific by adding redirect address variable
- Update CONTRIBUTORS
- Fix merge conflict (thanks @arledesma)
- Fix missed variable (thanks @arledesma)

## v1.2.9

- Fix backend template inclusion
- Correct backend filename

## v1.2.8

- Fix issue in wait_for (thanks @pierrefh)
- Add contributing guidelines in CONTRIBUTING.md
- Fix checksum var

## v1.2.7

- Update main tasks
- Update install tasks
- Prefer compact YAML format across all tasks files

## v1.2.6

- Check for local packages and summary files

## v1.2.5

- Updated configuration templates
- Updated documentation

## v1.2.4

- Vaule 0.6.5

## v1.2.3

- Vault 0.6.4

## v1.2.2

- Fix variable name

## v1.2.1

- Include installation tasks

## v1.2.0

- Vault 0.6.3
- Dynamic SHA
- Streamline tasks
- Streamline and consolidate variables
- Move OS variables to vars
- Separate install tasks
- Remove OS specific tasks
- Update documentation

## v1.0.21

- Update/validate CentOS 7 box
- Update documentation
- Update failure cases for CentOS
- Fix SysV init script

## v1.0.20

- Fix binary name


## v1.0.9

- Add files dir

## v1.0.8

- Add files dir

## v1.0.7

- Fix var names

## v1.0.6

- Add fail on old distro versions
- Remove all distro specific includes

## v1.0.5

- Remove unnecessary include

## v1.0.4

- Correct URL in docs
- Remove vars dir
- Enable download once / copy many install

## v1.1.2

- Move all vars to defaults
- Documentation updates

## v1.0.2

- Set correct RAM amount in Vagrantfile
- Rename Vagrant inventory back to cluster_nodes

## v1.0.2

- Update documentation

## v1.0.0

- Installs Vault
- Installs Vault with Consul backend onto Consul VMs from brianshumate.consul
