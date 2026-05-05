# BindDrift Ranked Warnings

## W-001797 SignatureDrift

- Risk: High
- Score: 13.8
- Symbol: vm_mmap
- Explanation: vm_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `16`

## W-000660 SignatureDrift

- Risk: High
- Score: 13.4
- Symbol: genphy_read_abilities
- Explanation: genphy_read_abilities changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `14`

## W-001823 SignatureDrift

- Risk: High
- Score: 13.2
- Symbol: vmalloc
- Explanation: vmalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `13`

## W-000798 SignatureDrift

- Risk: High
- Score: 13.0
- Symbol: kernel_read_file
- Explanation: kernel_read_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `12`

## W-001596 SignatureDrift

- Risk: High
- Score: 12.8
- Symbol: skb_copy
- Explanation: skb_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `11`

## W-001904 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: device
- Explanation: device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const core::ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut core::ffi::c_void'}, {'name': 'driver_data', 'type': '*mut core::ffi::c_void'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_ops', 'type': '*mut dma_map_ops'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'core::ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`

### Rust Evidence

- Graph edges: `50`

## W-001905 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: iov_iter
- Explanation: iov_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'iter_type', 'type': 'u8_'}, {'name': 'copy_mc', 'type': 'bool_'}, {'name': 'nofault', 'type': 'bool_'}, {'name': 'data_source', 'type': 'bool_'}, {'name': 'iov_offset', 'type': 'usize'}, {'name': '__bindgen_anon_1', 'type': 'iov_iter__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'iov_iter__bindgen_ty_2'}]`
- New: `[{'name': 'iter_type', 'type': 'u8_'}, {'name': 'nofault', 'type': 'bool_'}, {'name': 'data_source', 'type': 'bool_'}, {'name': 'iov_offset', 'type': 'usize'}, {'name': '__bindgen_anon_1', 'type': 'iov_iter__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'iov_iter__bindgen_ty_2'}]`

### Rust Evidence

- Graph edges: `20`

## W-000746 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: ioremap
- Explanation: ioremap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000530 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: early_memremap
- Explanation: early_memremap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000664 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: genphy_read_status
- Explanation: genphy_read_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000661 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: genphy_read_lpa
- Explanation: genphy_read_lpa changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000667 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: genphy_resume
- Explanation: genphy_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000669 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: genphy_soft_reset
- Explanation: genphy_soft_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000670 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: genphy_suspend
- Explanation: genphy_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000671 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: genphy_update_link
- Explanation: genphy_update_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000145 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: __vmalloc
- Explanation: __vmalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000160 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: _phy_start_aneg
- Explanation: _phy_start_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000398 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: devm_ioremap
- Explanation: devm_ioremap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000738 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: ioread64
- Explanation: ioread64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000762 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: iowrite64
- Explanation: iowrite64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000923 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: mdiobus_write
- Explanation: mdiobus_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000934 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: memremap
- Explanation: memremap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-001119 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: phy_init_hw
- Explanation: phy_init_hw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-001125 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: phy_modify
- Explanation: phy_modify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-001139 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: phy_read_paged
- Explanation: phy_read_paged changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-001929 FieldDrift

- Risk: High
- Score: 11.8
- Symbol: vm_fault
- Explanation: vm_fault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'vm_fault__bindgen_ty_1'}, {'name': 'flags', 'type': 'fault_flag'}, {'name': 'pmd', 'type': '*mut pmd_t'}, {'name': 'pud', 'type': '*mut pud_t'}, {'name': '__bindgen_anon_2', 'type': 'vm_fault__bindgen_ty_2'}, {'name': 'cow_page', 'type': '*mut page'}, {'name': 'page', 'type': '*mut page'}, {'name': 'pte', 'type': '*mut pte_t'}, {'name': 'ptl', 'type': '*mut spinlock_t'}, {'name': 'prealloc_pte', 'type': 'pgtable_t'}]`

### Rust Evidence

- Graph edges: `16`

## W-000201 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: autoneg
- Explanation: autoneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000497 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: dpm_resume
- Explanation: dpm_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000502 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: dpm_suspend
- Explanation: dpm_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000687 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: get_user_pages
- Explanation: get_user_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000916 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: mdiobus_read
- Explanation: mdiobus_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-001069 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: phy_attach
- Explanation: phy_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-001093 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: phy_drivers_unregister
- Explanation: phy_drivers_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-001146 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: phy_resolve_aneg_linkmode
- Explanation: phy_resolve_aneg_linkmode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-001165 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: phy_start
- Explanation: phy_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-001708 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: stack_trace_save
- Explanation: stack_trace_save changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000333 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: device_create
- Explanation: device_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000525 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: early_ioremap
- Explanation: early_ioremap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000578 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: find_vma
- Explanation: find_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000840 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: led_set_brightness
- Explanation: led_set_brightness changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000856 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: link
- Explanation: link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-001055 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: pci_iomap
- Explanation: pci_iomap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-001092 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: phy_drivers_register
- Explanation: phy_drivers_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-001188 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: pin_user_pages
- Explanation: pin_user_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-001587 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: skb_checksum
- Explanation: skb_checksum changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-001755 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: unpin_user_page
- Explanation: unpin_user_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-001842 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: vmemmap_populate
- Explanation: vmemmap_populate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-001852 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: vmf_insert_pfn
- Explanation: vmf_insert_pfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-001924 FieldDrift

- Risk: High
- Score: 11.4
- Symbol: sk_buff
- Explanation: sk_buff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'sk_buff__bindgen_ty_1'}, {'name': '__bindgen_anon_2', 'type': 'sk_buff__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'sk_buff__bindgen_ty_3'}, {'name': 'cb', 'type': '[core::ffi::c_char; 48usize]'}, {'name': '__bindgen_anon_4', 'type': 'sk_buff__bindgen_ty_4'}, {'name': '_nfct', 'type': 'core::ffi::c_ulong'}, {'name': 'len', 'type': 'core::ffi::c_uint'}, {'name': 'data_len', 'type': 'core::ffi::c_uint'}, {'name': 'mac_len', 'type': '__u16'}, {'name': 'hdr_len', 'type': '__u16'}, {'name': 'queue_mapping', 'type': '__u16'}, {'name': '__cloned_offset', 'type': '__IncompleteArrayField<__u8>'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'active_extensions', 'type': '__u8'}, {'name': '__bindgen_anon_5', 'type': 'sk_buff__bindgen_ty_5'}, {'name': 'tail', 'type': 'sk_buff_data_t'}, {'name': 'end', 'type': 'sk_buff_data_t'}, {'name': 'head', 'type': '*mut core::ffi::c_uchar'}, {'name': 'data', 'type': '*mut core::ffi::c_uchar'}, {'name': 'truesize', 'type': 'core::ffi::c_uint'}, {'name': 'users', 'type': 'refcount_t'}, {'name': 'extensions', 'type': '*mut skb_ext'}]`

### Rust Evidence

- Graph edges: `14`

## W-000027 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: __fdget
- Explanation: __fdget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000079 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: __phy_modify
- Explanation: __phy_modify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000116 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: __skb_checksum
- Explanation: __skb_checksum changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000194 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: arch_stack_walk
- Explanation: arch_stack_walk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000301 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: csum_partial
- Explanation: csum_partial changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000564 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: f_dupfd
- Explanation: f_dupfd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000567 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: fget
- Explanation: fget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000720 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: insert_resource
- Explanation: insert_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000732 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: ioread16
- Explanation: ioread16 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000735 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: ioread32
- Explanation: ioread32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000741 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: ioread64be
- Explanation: ioread64be changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000756 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: iowrite16
- Explanation: iowrite16 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000759 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: iowrite32
- Explanation: iowrite32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000765 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: iowrite64be
- Explanation: iowrite64be changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000827 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: led_blink_set
- Explanation: led_blink_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000994 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: netlink_broadcast
- Explanation: netlink_broadcast changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001140 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: phy_register_fixup
- Explanation: phy_register_fixup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001178 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: phy_unregister_fixup
- Explanation: phy_unregister_fixup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001197 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: pm_generic_freeze
- Explanation: pm_generic_freeze changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001200 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: pm_generic_poweroff
- Explanation: pm_generic_poweroff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001204 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: pm_generic_restore
- Explanation: pm_generic_restore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001207 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: pm_generic_resume
- Explanation: pm_generic_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001210 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: pm_generic_suspend
- Explanation: pm_generic_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001213 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: pm_generic_thaw
- Explanation: pm_generic_thaw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001539 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: sg_alloc_table
- Explanation: sg_alloc_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001564 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: sgl_free
- Explanation: sgl_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001639 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: skb_pull
- Explanation: skb_pull changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001672 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: skb_zerocopy
- Explanation: skb_zerocopy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001680 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: sock_create
- Explanation: sock_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001743 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: truncate_inode_pages
- Explanation: truncate_inode_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001749 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: type_
- Explanation: type_ changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'core::ffi::c_uint { unsafe { ::core::mem::transmute(self._bitfield_1.get(8usize, 3u8) as u32) } } #[inline] pub fn set_type(&mut self, val: core::ffi::c_uint) { unsafe { let val: u32 = ::core::mem::transmute(val)'}`
- New: `{'params': [{'name': '', 'type': '&self'}], 'return_type': 'u16_ { unsafe { ::core::mem::transmute(self._bitfield_1.get(8usize, 5u8) as u16) } } #[inline] pub fn set_type(&mut self, val: u16_) { unsafe { let val: u16 = ::core::mem::transmute(val)'}`

### Rust Evidence

- Graph edges: `3`

## W-001806 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: vm_unmapped_area
- Explanation: vm_unmapped_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001834 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: vmap
- Explanation: vmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000012 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __d_lookup
- Explanation: __d_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000054 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __mdiobus_modify
- Explanation: __mdiobus_modify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000066 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __ndelay
- Explanation: __ndelay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000080 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __phy_modify_mmd
- Explanation: __phy_modify_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000093 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __pte_alloc
- Explanation: __pte_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000095 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __pte_offset_map
- Explanation: __pte_offset_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000117 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __skb_checksum_complete
- Explanation: __skb_checksum_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000126 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __skb_get_hash
- Explanation: __skb_get_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000147 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __vmalloc_node
- Explanation: __vmalloc_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000166 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: active
- Explanation: active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000188 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: arch_irq_stat
- Explanation: arch_irq_stat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000205 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bpf_flow_dissect
- Explanation: bpf_flow_dissect changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000206 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: build_skb
- Explanation: build_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000214 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bus_register
- Explanation: bus_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000219 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bus_unregister
- Explanation: bus_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000223 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: calibrate_delay
- Explanation: calibrate_delay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000262 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: class_create
- Explanation: class_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000278 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: cloned
- Explanation: cloned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000328 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: device_add
- Explanation: device_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000341 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: device_find_child
- Explanation: device_find_child changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000343 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: device_for_each_child
- Explanation: device_for_each_child changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000363 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: device_phy_find_device
- Explanation: device_phy_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000370 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: device_remove_file
- Explanation: device_remove_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000391 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: devm_device_add_group
- Explanation: devm_device_add_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000400 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: devm_ioremap_resource
- Explanation: devm_ioremap_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000410 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: devm_kstrdup
- Explanation: devm_kstrdup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000421 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: devm_of_led_get
- Explanation: devm_of_led_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000437 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: devres_release
- Explanation: devres_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000439 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: devres_remove
- Explanation: devres_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000512 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: driver_find
- Explanation: driver_find changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000562 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: expand_stack
- Explanation: expand_stack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000611 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: fwnode_get_phy_node
- Explanation: fwnode_get_phy_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000615 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: fwnode_phy_find_device
- Explanation: fwnode_phy_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000677 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: get_device
- Explanation: get_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000682 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: get_phy_device
- Explanation: get_phy_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000688 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: get_user_pages_fast
- Explanation: get_user_pages_fast changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000692 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: get_vm_area
- Explanation: get_vm_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000710 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: in_gate_area
- Explanation: in_gate_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000744 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: ioread8
- Explanation: ioread8 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000768 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: iowrite8
- Explanation: iowrite8 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000772 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: irq_enter
- Explanation: irq_enter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000774 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: irq_exit
- Explanation: irq_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000783 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: is_kernel
- Explanation: is_kernel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000800 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kernel_read_file_from_path
- Explanation: kernel_read_file_from_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000803 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: kernel_sendmsg
- Explanation: kernel_sendmsg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000818 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: klist_iter_init
- Explanation: klist_iter_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000835 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: led_get
- Explanation: led_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000844 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: led_trigger_blink
- Explanation: led_trigger_blink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000847 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: led_trigger_register
- Explanation: led_trigger_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000850 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: led_trigger_set
- Explanation: led_trigger_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000852 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: led_trigger_unregister
- Explanation: led_trigger_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000859 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: list_lru_add
- Explanation: list_lru_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'lru', 'type': '*mut list_lru'}, {'name': 'item', 'type': '*mut list_head'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'lru', 'type': '*mut list_lru'}, {'name': 'item', 'type': '*mut list_head'}, {'name': 'nid', 'type': 'core::ffi::c_int'}, {'name': 'memcg', 'type': '*mut mem_cgroup'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `2`

## W-000861 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: list_lru_del
- Explanation: list_lru_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'lru', 'type': '*mut list_lru'}, {'name': 'item', 'type': '*mut list_head'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'lru', 'type': '*mut list_lru'}, {'name': 'item', 'type': '*mut list_head'}, {'name': 'nid', 'type': 'core::ffi::c_int'}, {'name': 'memcg', 'type': '*mut mem_cgroup'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `2`

## W-000864 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: lock_device_hotplug
- Explanation: lock_device_hotplug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000882 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mask
- Explanation: mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000905 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mdiobus_c45_modify
- Explanation: mdiobus_c45_modify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000907 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mdiobus_c45_read
- Explanation: mdiobus_c45_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000909 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mdiobus_c45_write
- Explanation: mdiobus_c45_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000914 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mdiobus_modify
- Explanation: mdiobus_modify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000921 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: mdiobus_unregister
- Explanation: mdiobus_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000932 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: memory_failure
- Explanation: memory_failure changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000970 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: msleep
- Explanation: msleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001020 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: no_pm
- Explanation: no_pm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001023 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: node_page_state
- Explanation: node_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001034 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: offline
- Explanation: offline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001053 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: partition_sched_domains
- Explanation: partition_sched_domains changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001057 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pci_iomap_wc
- Explanation: pci_iomap_wc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001071 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: phy_attached_info
- Explanation: phy_attached_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001077 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: phy_connect
- Explanation: phy_connect changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001081 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: phy_device_free
- Explanation: phy_device_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001086 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: phy_do_ioctl
- Explanation: phy_do_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001088 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: phy_driver_is_genphy
- Explanation: phy_driver_is_genphy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001123 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: phy_mac_interrupt
- Explanation: phy_mac_interrupt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001127 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: phy_modify_mmd
- Explanation: phy_modify_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001129 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: phy_modify_paged
- Explanation: phy_modify_paged changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001160 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: phy_speed_down
- Explanation: phy_speed_down changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001167 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: phy_start_cable_test
- Explanation: phy_start_cable_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001171 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: phy_stop
- Explanation: phy_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001192 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pkt_type
- Explanation: pkt_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001228 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pmdp_invalidate
- Explanation: pmdp_invalidate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001242 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: ptep_clear_flush
- Explanation: ptep_clear_flush changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001259 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: receive_fd
- Explanation: receive_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001264 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: region_intersects
- Explanation: region_intersects changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001271 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: remap_pfn_range
- Explanation: remap_pfn_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001273 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: remap_vmalloc_range
- Explanation: remap_vmalloc_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001283 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: request_resource
- Explanation: request_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001297 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: scm_detach_fds
- Explanation: scm_detach_fds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001328 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: security_file_ioctl
- Explanation: security_file_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001349 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: security_inode_copy_up
- Explanation: security_inode_copy_up changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001360 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: security_inode_init_security
- Explanation: security_inode_init_security changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001508 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: security_tun_dev_attach
- Explanation: security_tun_dev_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001526 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: set_page_dirty
- Explanation: set_page_dirty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001546 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sg_free_table
- Explanation: sg_free_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001555 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sg_nents
- Explanation: sg_nents changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001562 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sgl_alloc
- Explanation: sgl_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001572 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: si_meminfo
- Explanation: si_meminfo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001584 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: skb_append
- Explanation: skb_append changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001590 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: skb_clone
- Explanation: skb_clone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001608 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: skb_dequeue
- Explanation: skb_dequeue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001611 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: skb_ensure_writable
- Explanation: skb_ensure_writable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001652 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: skb_segment
- Explanation: skb_segment changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001654 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: skb_send_sock
- Explanation: skb_send_sock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001662 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: skb_to_sgvec
- Explanation: skb_to_sgvec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001678 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: sock_alloc
- Explanation: sock_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001703 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: stack_depot_save
- Explanation: stack_depot_save changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001710 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: stack_trace_save_tsk
- Explanation: stack_trace_save_tsk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001723 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: suspended
- Explanation: suspended changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001735 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: tc_at_ingress
- Explanation: tc_at_ingress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001746 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: truncate_pagecache
- Explanation: truncate_pagecache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001757 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: unpin_user_pages
- Explanation: unpin_user_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001763 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: untrack_pfn
- Explanation: untrack_pfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001778 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vfree
- Explanation: vfree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001791 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vm_insert_page
- Explanation: vm_insert_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001794 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vm_map_pages
- Explanation: vm_map_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001799 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vm_normal_folio
- Explanation: vm_normal_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001801 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vm_normal_page
- Explanation: vm_normal_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001808 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vma_interval_tree_insert
- Explanation: vma_interval_tree_insert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001824 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vmalloc_32
- Explanation: vmalloc_32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001836 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vmemmap_alloc_block
- Explanation: vmemmap_alloc_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001850 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vmf_insert_mixed
- Explanation: vmf_insert_mixed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001858 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vunmap
- Explanation: vunmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001860 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: vzalloc
- Explanation: vzalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001879 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: walk_system_ram_res
- Explanation: walk_system_ram_res changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001882 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: wifi_acked
- Explanation: wifi_acked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-001892 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: zerocopy
- Explanation: zerocopy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000001 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: BUG_func
- Explanation: BUG_func changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ___pskb_trim
- Explanation: ___pskb_trim changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __absent_pages_in_range
- Explanation: __absent_pages_in_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __account_locked_vm
- Explanation: __account_locked_vm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000005 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __alloc_skb
- Explanation: __alloc_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000006 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bad_mask
- Explanation: __bad_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bad_ndelay
- Explanation: __bad_ndelay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bad_udelay
- Explanation: __bad_udelay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __build_skb
- Explanation: __build_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __const_udelay
- Explanation: __const_udelay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000011 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __consume_stateless_skb
- Explanation: __consume_stateless_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __dec_node_page_state
- Explanation: __dec_node_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __dec_node_state
- Explanation: __dec_node_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000016 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __dec_zone_page_state
- Explanation: __dec_zone_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __dec_zone_state
- Explanation: __dec_zone_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __delay
- Explanation: __delay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __devm_add_action
- Explanation: __devm_add_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000020 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __devm_alloc_percpu
- Explanation: __devm_alloc_percpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000021 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __devm_mdiobus_register
- Explanation: __devm_mdiobus_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __devm_release_region
- Explanation: __devm_release_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000023 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __devm_request_region
- Explanation: __devm_request_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __devres_alloc_node
- Explanation: __devres_alloc_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ethtool_get_link_ksettings
- Explanation: __ethtool_get_link_ksettings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __f_unlock_pos
- Explanation: __f_unlock_pos changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __fdget_pos
- Explanation: __fdget_pos changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __fdget_raw
- Explanation: __fdget_raw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000030 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __field_overflow
- Explanation: __field_overflow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __folio_put
- Explanation: __folio_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __folio_start_writeback
- Explanation: __folio_start_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'folio', 'type': '*mut folio'}, {'name': 'keep_write', 'type': 'bool_'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'folio', 'type': '*mut folio'}, {'name': 'keep_write', 'type': 'bool_'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __fput_sync
- Explanation: __fput_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000034 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __genphy_config_aneg
- Explanation: __genphy_config_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_compat_msghdr
- Explanation: __get_compat_msghdr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_hash_from_flowi6
- Explanation: __get_hash_from_flowi6 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_locked_pte
- Explanation: __get_locked_pte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_unused_fd_flags
- Explanation: __get_unused_fd_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __get_vm_area_caller
- Explanation: __get_vm_area_caller changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __hsiphash_aligned
- Explanation: __hsiphash_aligned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __hsiphash_unaligned
- Explanation: __hsiphash_unaligned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __inc_node_page_state
- Explanation: __inc_node_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000044 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __inc_node_state
- Explanation: __inc_node_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __inc_zone_page_state
- Explanation: __inc_zone_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __inc_zone_state
- Explanation: __inc_zone_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __ioread32_copy
- Explanation: __ioread32_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __iowrite32_copy
- Explanation: __iowrite32_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000049 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __iowrite64_copy
- Explanation: __iowrite64_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000050 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kernel_map_pages
- Explanation: __kernel_map_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __kfree_skb
- Explanation: __kfree_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mdiobus_c45_read
- Explanation: __mdiobus_c45_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000053 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mdiobus_c45_write
- Explanation: __mdiobus_c45_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000055 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mdiobus_modify_changed
- Explanation: __mdiobus_modify_changed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mdiobus_read
- Explanation: __mdiobus_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000057 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mdiobus_register
- Explanation: __mdiobus_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000058 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mdiobus_write
- Explanation: __mdiobus_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000059 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mm_populate
- Explanation: __mm_populate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mod_node_page_state
- Explanation: __mod_node_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000061 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mod_zone_page_state
- Explanation: __mod_zone_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000062 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __mt_dup
- Explanation: __mt_dup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __napi_alloc_frag_align
- Explanation: __napi_alloc_frag_align changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __napi_alloc_skb
- Explanation: __napi_alloc_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __napi_kfree_skb
- Explanation: __napi_kfree_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000067 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __netdev_alloc_frag_align
- Explanation: __netdev_alloc_frag_align changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __netdev_alloc_skb
- Explanation: __netdev_alloc_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000069 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __netlink_change_ngroups
- Explanation: __netlink_change_ngroups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __netlink_clear_multicast_users
- Explanation: __netlink_clear_multicast_users changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __netlink_dump_start
- Explanation: __netlink_dump_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __netlink_kernel_create
- Explanation: __netlink_kernel_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000073 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __netlink_ns_capable
- Explanation: __netlink_ns_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000074 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __nlmsg_put
- Explanation: __nlmsg_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000075 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __p4d_alloc
- Explanation: __p4d_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000076 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __page_file_index
- Explanation: __page_file_index changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000077 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __phy_hwtstamp_get
- Explanation: __phy_hwtstamp_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000078 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __phy_hwtstamp_set
- Explanation: __phy_hwtstamp_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000081 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __phy_modify_mmd_changed
- Explanation: __phy_modify_mmd_changed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000082 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __phy_package_read_mmd
- Explanation: __phy_package_read_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __phy_package_write_mmd
- Explanation: __phy_package_write_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __phy_read_mmd
- Explanation: __phy_read_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000085 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __phy_resume
- Explanation: __phy_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000086 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __phy_write_mmd
- Explanation: __phy_write_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000087 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pm_relax
- Explanation: __pm_relax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000088 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pm_stay_awake
- Explanation: __pm_stay_awake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000089 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pmd_alloc
- Explanation: __pmd_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __populate_section_memmap
- Explanation: __populate_section_memmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pskb_copy_fclone
- Explanation: __pskb_copy_fclone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000092 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pskb_pull_tail
- Explanation: __pskb_pull_tail changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pte_alloc_kernel
- Explanation: __pte_alloc_kernel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pte_offset_map_lock
- Explanation: __pte_offset_map_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000097 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __pud_alloc
- Explanation: __pud_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __release_region
- Explanation: __release_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __request_region
- Explanation: __request_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000103 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __root_device_register
- Explanation: __root_device_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __scm_destroy
- Explanation: __scm_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __scm_send
- Explanation: __scm_send changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000108 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sg_alloc_table
- Explanation: __sg_alloc_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sg_free_table
- Explanation: __sg_free_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sg_page_iter_dma_next
- Explanation: __sg_page_iter_dma_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sg_page_iter_next
- Explanation: __sg_page_iter_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000112 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sg_page_iter_start
- Explanation: __sg_page_iter_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000113 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __show_mem
- Explanation: __show_mem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000114 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __siphash_aligned
- Explanation: __siphash_aligned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000115 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __siphash_unaligned
- Explanation: __siphash_unaligned changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000118 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_checksum_complete_head
- Explanation: __skb_checksum_complete_head changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000119 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_ext_alloc
- Explanation: __skb_ext_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000120 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_ext_del
- Explanation: __skb_ext_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000121 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_ext_put
- Explanation: __skb_ext_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000122 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_ext_set
- Explanation: __skb_ext_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000123 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_flow_dissect
- Explanation: __skb_flow_dissect changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000124 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_flow_get_ports
- Explanation: __skb_flow_get_ports changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000125 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_free_datagram_locked
- Explanation: __skb_free_datagram_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000127 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_get_hash_symmetric
- Explanation: __skb_get_hash_symmetric changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_get_poff
- Explanation: __skb_get_poff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000129 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_pad
- Explanation: __skb_pad changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000130 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_recv_datagram
- Explanation: __skb_recv_datagram changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000131 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_try_recv_datagram
- Explanation: __skb_try_recv_datagram changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_try_recv_from_queue
- Explanation: __skb_try_recv_from_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_tstamp_tx
- Explanation: __skb_tstamp_tx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000134 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_unclone_keeptruesize
- Explanation: __skb_unclone_keeptruesize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_vlan_pop
- Explanation: __skb_vlan_pop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000136 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_wait_for_more_packets
- Explanation: __skb_wait_for_more_packets changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_warn_lro_forwarding
- Explanation: __skb_warn_lro_forwarding changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_zcopy_downgrade_managed
- Explanation: __skb_zcopy_downgrade_managed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000139 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __sock_create
- Explanation: __sock_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000140 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __suspend_report_result
- Explanation: __suspend_report_result changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000141 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __udelay
- Explanation: __udelay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000142 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __vcalloc
- Explanation: __vcalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000143 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __vm_area_free
- Explanation: __vm_area_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000144 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __vm_enough_memory
- Explanation: __vm_enough_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000146 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __vmalloc_array
- Explanation: __vmalloc_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000148 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __vmalloc_node_range
- Explanation: __vmalloc_node_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __zerocopy_sg_from_iter
- Explanation: __zerocopy_sg_from_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _dev_alert
- Explanation: _dev_alert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000151 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _dev_crit
- Explanation: _dev_crit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _dev_emerg
- Explanation: _dev_emerg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000153 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _dev_err
- Explanation: _dev_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _dev_info
- Explanation: _dev_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _dev_notice
- Explanation: _dev_notice changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _dev_printk
- Explanation: _dev_printk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _dev_warn
- Explanation: _dev_warn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _install_special_mapping
- Explanation: _install_special_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: absent_pages_in_range
- Explanation: absent_pages_in_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: access_process_vm
- Explanation: access_process_vm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: access_remote_vm
- Explanation: access_remote_vm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: account_locked_vm
- Explanation: account_locked_vm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ack_bad_irq
- Explanation: ack_bad_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000167 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: active_low
- Explanation: active_low changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: adjust_managed_page_count
- Explanation: adjust_managed_page_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000169 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: adjust_resource
- Explanation: adjust_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000170 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: all_vm_events
- Explanation: all_vm_events changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_file_clone
- Explanation: alloc_file_clone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_file_pseudo
- Explanation: alloc_file_pseudo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_free_mem_region
- Explanation: alloc_free_mem_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_sched_domains
- Explanation: alloc_sched_domains changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_skb_for_msg
- Explanation: alloc_skb_for_msg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_skb_with_frags
- Explanation: alloc_skb_with_frags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000177 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: allocate_resource
- Explanation: allocate_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000178 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: anon_vma_interval_tree_insert
- Explanation: anon_vma_interval_tree_insert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000179 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: anon_vma_interval_tree_iter_first
- Explanation: anon_vma_interval_tree_iter_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000180 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: anon_vma_interval_tree_iter_next
- Explanation: anon_vma_interval_tree_iter_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: anon_vma_interval_tree_remove
- Explanation: anon_vma_interval_tree_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: apply_to_existing_page_range
- Explanation: apply_to_existing_page_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000184 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: apply_to_page_range
- Explanation: apply_to_page_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000185 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_asym_cpu_priority
- Explanation: arch_asym_cpu_priority changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000186 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_io_free_memtype_wc
- Explanation: arch_io_free_memtype_wc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000187 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_io_reserve_memtype_wc
- Explanation: arch_io_reserve_memtype_wc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_irq_stat_cpu
- Explanation: arch_irq_stat_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000190 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_phys_wc_add
- Explanation: arch_phys_wc_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000191 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_phys_wc_del
- Explanation: arch_phys_wc_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000192 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_phys_wc_index
- Explanation: arch_phys_wc_index changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000193 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_remove_reservations
- Explanation: arch_remove_reservations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000195 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_stack_walk_reliable
- Explanation: arch_stack_walk_reliable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000196 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_stack_walk_user
- Explanation: arch_stack_walk_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000197 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_sync_kernel_mappings
- Explanation: arch_sync_kernel_mappings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000198 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_vma_name
- Explanation: arch_vma_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: async_in_progress
- Explanation: async_in_progress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000200 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: async_suspend
- Explanation: async_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000202 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: autoneg_complete
- Explanation: autoneg_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000203 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: autosleep_enabled
- Explanation: autosleep_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000207 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: build_skb_around
- Explanation: build_skb_around changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000208 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_create_file
- Explanation: bus_create_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000209 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_find_device
- Explanation: bus_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000210 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_for_each_dev
- Explanation: bus_for_each_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000211 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_for_each_drv
- Explanation: bus_for_each_drv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000212 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_get_dev_root
- Explanation: bus_get_dev_root changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000213 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_get_kset
- Explanation: bus_get_kset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000215 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_register_notifier
- Explanation: bus_register_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000216 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_remove_file
- Explanation: bus_remove_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000217 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_rescan_devices
- Explanation: bus_rescan_devices changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000218 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_sort_breadthfirst
- Explanation: bus_sort_breadthfirst changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000220 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bus_unregister_notifier
- Explanation: bus_unregister_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000221 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: calculate_normal_threshold
- Explanation: calculate_normal_threshold changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000222 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: calculate_pressure_threshold
- Explanation: calculate_pressure_threshold changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000224 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: calibrate_delay_is_known
- Explanation: calibrate_delay_is_known changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: calibration_delay_done
- Explanation: calibration_delay_done changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000226 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: call_blocking_lsm_notifier
- Explanation: call_blocking_lsm_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000227 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: can_change_pte_writable
- Explanation: can_change_pte_writable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000228 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: can_do_mlock
- Explanation: can_do_mlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000229 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: can_match
- Explanation: can_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000230 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: can_wakeup
- Explanation: can_wakeup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000231 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_bprm_creds_from_file
- Explanation: cap_bprm_creds_from_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000232 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_capable
- Explanation: cap_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000233 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_capget
- Explanation: cap_capget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000234 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_capset
- Explanation: cap_capset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000235 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_inode_getsecurity
- Explanation: cap_inode_getsecurity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000236 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_inode_killpriv
- Explanation: cap_inode_killpriv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000237 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_inode_need_killpriv
- Explanation: cap_inode_need_killpriv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000238 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_inode_removexattr
- Explanation: cap_inode_removexattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000239 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_inode_setxattr
- Explanation: cap_inode_setxattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000240 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_link_lanes_supported
- Explanation: cap_link_lanes_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000241 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_mmap_addr
- Explanation: cap_mmap_addr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000242 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_mmap_file
- Explanation: cap_mmap_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_ptrace_access_check
- Explanation: cap_ptrace_access_check changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_ptrace_traceme
- Explanation: cap_ptrace_traceme changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000245 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_rss_ctx_supported
- Explanation: cap_rss_ctx_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000246 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_rss_sym_xor_supported
- Explanation: cap_rss_sym_xor_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000247 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_settime
- Explanation: cap_settime changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000248 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_task_fix_setuid
- Explanation: cap_task_fix_setuid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000249 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_task_prctl
- Explanation: cap_task_prctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000250 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_task_setioprio
- Explanation: cap_task_setioprio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000251 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_task_setnice
- Explanation: cap_task_setnice changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000252 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_task_setscheduler
- Explanation: cap_task_setscheduler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000253 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cap_vm_enough_memory
- Explanation: cap_vm_enough_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000254 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: change_huge_pmd
- Explanation: change_huge_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000255 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: change_protection
- Explanation: change_protection changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000257 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: check_signature
- Explanation: check_signature changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000258 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_compat_create_link
- Explanation: class_compat_create_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000259 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_compat_register
- Explanation: class_compat_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000260 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_compat_remove_link
- Explanation: class_compat_remove_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000261 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_compat_unregister
- Explanation: class_compat_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000263 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_create_file_ns
- Explanation: class_create_file_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000264 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_destroy
- Explanation: class_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000265 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_dev_iter_exit
- Explanation: class_dev_iter_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000266 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_dev_iter_init
- Explanation: class_dev_iter_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000267 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_dev_iter_next
- Explanation: class_dev_iter_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000268 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_find_device
- Explanation: class_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000269 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_for_each_device
- Explanation: class_for_each_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000270 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_interface_register
- Explanation: class_interface_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000271 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_interface_unregister
- Explanation: class_interface_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000272 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_is_registered
- Explanation: class_is_registered changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000273 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_register
- Explanation: class_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000274 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_remove_file_ns
- Explanation: class_remove_file_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000275 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: class_unregister
- Explanation: class_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000276 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: clear_huge_page
- Explanation: clear_huge_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000277 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: clflush_cache_range
- Explanation: clflush_cache_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000279 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cmsghdr_from_user_compat_to_kern
- Explanation: cmsghdr_from_user_compat_to_kern changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000280 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: consume_skb
- Explanation: consume_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000281 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_folio_from_user
- Explanation: copy_folio_from_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000282 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_from_early_mem
- Explanation: copy_from_early_mem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000283 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_huge_pmd
- Explanation: copy_huge_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000284 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_huge_pud
- Explanation: copy_huge_pud changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000285 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_namespaces
- Explanation: copy_namespaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000286 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_page_range
- Explanation: copy_page_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000287 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_user_large_folio
- Explanation: copy_user_large_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000288 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_vma
- Explanation: copy_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000289 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_vm_stats_fold
- Explanation: cpu_vm_stats_fold changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000290 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_add_update_util_hook
- Explanation: cpufreq_add_update_util_hook changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000291 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_remove_update_util_hook
- Explanation: cpufreq_remove_update_util_hook changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000292 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_this_cpu_can_update
- Explanation: cpufreq_this_cpu_can_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000293 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpus_share_cache
- Explanation: cpus_share_cache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000294 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpus_share_resources
- Explanation: cpus_share_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000295 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: csum_and_copy_from_iter_full
- Explanation: csum_and_copy_from_iter_full changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000296 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: csum_and_copy_from_user
- Explanation: csum_and_copy_from_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000297 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: csum_and_copy_to_user
- Explanation: csum_and_copy_to_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000298 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: csum_complete_sw
- Explanation: csum_complete_sw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000299 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: csum_ipv6_magic
- Explanation: csum_ipv6_magic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000300 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: csum_level
- Explanation: csum_level changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000302 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: csum_partial_copy_generic
- Explanation: csum_partial_copy_generic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000303 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: csum_partial_copy_nocheck
- Explanation: csum_partial_copy_nocheck changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000304 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: csum_valid
- Explanation: csum_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000309 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: datagram_poll
- Explanation: datagram_poll changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000310 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dec_node_page_state
- Explanation: dec_node_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000311 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dec_zone_page_state
- Explanation: dec_zone_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000312 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dec_zone_state
- Explanation: dec_zone_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000313 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: default_state
- Explanation: default_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000314 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: deferred_resume
- Explanation: deferred_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000318 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: destroy_large_folio
- Explanation: destroy_large_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000319 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_driver_string
- Explanation: dev_driver_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000320 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_err_probe
- Explanation: dev_err_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000321 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_get_subsys_data
- Explanation: dev_pm_get_subsys_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000322 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_put_subsys_data
- Explanation: dev_pm_put_subsys_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000323 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_skip_resume
- Explanation: dev_pm_skip_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000324 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_skip_suspend
- Explanation: dev_pm_skip_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000325 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_printk_emit
- Explanation: dev_printk_emit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000326 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_set_name
- Explanation: dev_set_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000327 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_vprintk_emit
- Explanation: dev_vprintk_emit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000329 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_add_groups
- Explanation: device_add_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000330 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_attach
- Explanation: device_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000331 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_bind_driver
- Explanation: device_bind_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000332 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_change_owner
- Explanation: device_change_owner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000334 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_create_bin_file
- Explanation: device_create_bin_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000335 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_create_file
- Explanation: device_create_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000336 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_create_with_groups
- Explanation: device_create_with_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000337 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_del
- Explanation: device_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000338 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_destroy
- Explanation: device_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000339 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_driver_attach
- Explanation: device_driver_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000340 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_find_any_child
- Explanation: device_find_any_child changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000342 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_find_child_by_name
- Explanation: device_find_child_by_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000344 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_for_each_child_reverse
- Explanation: device_for_each_child_reverse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000345 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_initial_probe
- Explanation: device_initial_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000346 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_initialize
- Explanation: device_initialize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000347 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_is_bound
- Explanation: device_is_bound changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000348 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_link_add
- Explanation: device_link_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000349 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_link_del
- Explanation: device_link_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000350 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_link_remove
- Explanation: device_link_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000351 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_links_supplier_sync_state_pause
- Explanation: device_links_supplier_sync_state_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000352 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_links_supplier_sync_state_resume
- Explanation: device_links_supplier_sync_state_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000353 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_match_acpi_dev
- Explanation: device_match_acpi_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000354 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_match_acpi_handle
- Explanation: device_match_acpi_handle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000355 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_match_any
- Explanation: device_match_any changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000356 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_match_devt
- Explanation: device_match_devt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000357 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_match_fwnode
- Explanation: device_match_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000358 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_match_name
- Explanation: device_match_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000359 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_match_of_node
- Explanation: device_match_of_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000360 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_move
- Explanation: device_move changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000361 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_offline
- Explanation: device_offline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000362 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_online
- Explanation: device_online changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000364 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_pm_lock
- Explanation: device_pm_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000365 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_pm_unlock
- Explanation: device_pm_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000366 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_pm_wait_for_dev
- Explanation: device_pm_wait_for_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000367 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_register
- Explanation: device_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000368 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_release_driver
- Explanation: device_release_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000369 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_remove_bin_file
- Explanation: device_remove_bin_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000371 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_remove_file_self
- Explanation: device_remove_file_self changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000372 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_remove_groups
- Explanation: device_remove_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000373 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_rename
- Explanation: device_rename changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000374 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_reprobe
- Explanation: device_reprobe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000375 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_set_node
- Explanation: device_set_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000376 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_set_of_node_from_dev
- Explanation: device_set_of_node_from_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000377 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_set_wakeup_capable
- Explanation: device_set_wakeup_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000378 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_set_wakeup_enable
- Explanation: device_set_wakeup_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000379 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_show_bool
- Explanation: device_show_bool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000380 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_show_int
- Explanation: device_show_int changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000381 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_show_ulong
- Explanation: device_show_ulong changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000382 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_shutdown
- Explanation: device_shutdown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000383 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_store_bool
- Explanation: device_store_bool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000384 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_store_int
- Explanation: device_store_int changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000385 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_store_ulong
- Explanation: device_store_ulong changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000386 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_unregister
- Explanation: device_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000387 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_wakeup_disable
- Explanation: device_wakeup_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000388 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: device_wakeup_enable
- Explanation: device_wakeup_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000389 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_arch_io_reserve_memtype_wc
- Explanation: devm_arch_io_reserve_memtype_wc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000390 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_arch_phys_wc_add
- Explanation: devm_arch_phys_wc_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000392 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_device_add_groups
- Explanation: devm_device_add_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000393 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_free_pages
- Explanation: devm_free_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000394 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_free_percpu
- Explanation: devm_free_percpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000395 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_get_free_pages
- Explanation: devm_get_free_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000396 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_ioport_map
- Explanation: devm_ioport_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000397 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_ioport_unmap
- Explanation: devm_ioport_unmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000399 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_ioremap_release
- Explanation: devm_ioremap_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000401 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_ioremap_resource_wc
- Explanation: devm_ioremap_resource_wc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000402 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_ioremap_uc
- Explanation: devm_ioremap_uc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000403 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_ioremap_wc
- Explanation: devm_ioremap_wc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000404 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_iounmap
- Explanation: devm_iounmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000405 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_kasprintf
- Explanation: devm_kasprintf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000406 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_kfree
- Explanation: devm_kfree changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000407 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_kmalloc
- Explanation: devm_kmalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000408 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_kmemdup
- Explanation: devm_kmemdup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000409 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_krealloc
- Explanation: devm_krealloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000411 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_kstrdup_const
- Explanation: devm_kstrdup_const changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000412 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_kvasprintf
- Explanation: devm_kvasprintf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000413 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_led_classdev_register_ext
- Explanation: devm_led_classdev_register_ext changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000414 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_led_classdev_unregister
- Explanation: devm_led_classdev_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000415 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_led_get
- Explanation: devm_led_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000416 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_led_trigger_register
- Explanation: devm_led_trigger_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000417 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_mdiobus_alloc_size
- Explanation: devm_mdiobus_alloc_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000418 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_memremap
- Explanation: devm_memremap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000419 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_memunmap
- Explanation: devm_memunmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000420 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_of_iomap
- Explanation: devm_of_iomap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000422 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_of_led_get_optional
- Explanation: devm_of_led_get_optional changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000423 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_phy_package_join
- Explanation: devm_phy_package_join changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000424 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_release_action
- Explanation: devm_release_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000425 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_release_resource
- Explanation: devm_release_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000426 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_remove_action
- Explanation: devm_remove_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000427 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_request_free_mem_region
- Explanation: devm_request_free_mem_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000428 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_request_resource
- Explanation: devm_request_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000429 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devres_add
- Explanation: devres_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000430 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devres_close_group
- Explanation: devres_close_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000431 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devres_destroy
- Explanation: devres_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000432 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devres_find
- Explanation: devres_find changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000433 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devres_for_each_res
- Explanation: devres_for_each_res changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000434 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devres_free
- Explanation: devres_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000435 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devres_get
- Explanation: devres_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000436 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devres_open_group
- Explanation: devres_open_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000438 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devres_release_group
- Explanation: devres_release_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000440 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devres_remove_group
- Explanation: devres_remove_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000441 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devtmpfs_mount
- Explanation: devtmpfs_mount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000442 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: direct_complete
- Explanation: direct_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000443 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disable_depth
- Explanation: disable_depth changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000445 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dl_server
- Explanation: dl_server changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000446 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_addressing_limited
- Explanation: dma_addressing_limited changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000447 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_alloc_attrs
- Explanation: dma_alloc_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000448 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_alloc_noncontiguous
- Explanation: dma_alloc_noncontiguous changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000449 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_alloc_pages
- Explanation: dma_alloc_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000450 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_can_mmap
- Explanation: dma_can_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000451 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_coherent_ok
- Explanation: dma_coherent_ok changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000452 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_free_attrs
- Explanation: dma_free_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000453 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_free_noncontiguous
- Explanation: dma_free_noncontiguous changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000454 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_free_pages
- Explanation: dma_free_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000455 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_get_merge_boundary
- Explanation: dma_get_merge_boundary changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000456 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_get_required_mask
- Explanation: dma_get_required_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000457 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_get_sgtable_attrs
- Explanation: dma_get_sgtable_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000458 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_map_page_attrs
- Explanation: dma_map_page_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000459 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_map_resource
- Explanation: dma_map_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000460 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_map_sg_attrs
- Explanation: dma_map_sg_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000461 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_map_sgtable
- Explanation: dma_map_sgtable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000462 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_max_mapping_size
- Explanation: dma_max_mapping_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000463 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_mmap_attrs
- Explanation: dma_mmap_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000464 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_mmap_noncontiguous
- Explanation: dma_mmap_noncontiguous changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000465 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_mmap_pages
- Explanation: dma_mmap_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000466 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_need_sync
- Explanation: dma_need_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000467 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_opt_mapping_size
- Explanation: dma_opt_mapping_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000468 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_pci_p2pdma_supported
- Explanation: dma_pci_p2pdma_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000469 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_set_coherent_mask
- Explanation: dma_set_coherent_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000470 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_set_mask
- Explanation: dma_set_mask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000471 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_sync_sg_for_cpu
- Explanation: dma_sync_sg_for_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000472 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_sync_sg_for_device
- Explanation: dma_sync_sg_for_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000473 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_sync_single_for_cpu
- Explanation: dma_sync_single_for_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000474 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_sync_single_for_device
- Explanation: dma_sync_single_for_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000475 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_unmap_page_attrs
- Explanation: dma_unmap_page_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000476 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_unmap_resource
- Explanation: dma_unmap_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000477 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_unmap_sg_attrs
- Explanation: dma_unmap_sg_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000478 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_vmap_noncontiguous
- Explanation: dma_vmap_noncontiguous changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000479 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_vunmap_noncontiguous
- Explanation: dma_vunmap_noncontiguous changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000480 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dmam_alloc_attrs
- Explanation: dmam_alloc_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000481 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dmam_free_coherent
- Explanation: dmam_free_coherent changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000483 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_huge_pmd_anonymous_page
- Explanation: do_huge_pmd_anonymous_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000484 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_huge_pmd_wp_page
- Explanation: do_huge_pmd_wp_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000485 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_madvise
- Explanation: do_madvise changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000486 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_mmap
- Explanation: do_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000487 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_munmap
- Explanation: do_munmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000488 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_set_pmd
- Explanation: do_set_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000490 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_trace_netlink_extack
- Explanation: do_trace_netlink_extack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000491 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_vma_munmap
- Explanation: do_vma_munmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000492 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_vmi_munmap
- Explanation: do_vmi_munmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000493 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: downshifted_rate
- Explanation: downshifted_rate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000494 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_complete
- Explanation: dpm_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000495 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_for_each_dev
- Explanation: dpm_for_each_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000496 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_prepare
- Explanation: dpm_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000498 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_resume_early
- Explanation: dpm_resume_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000499 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_resume_end
- Explanation: dpm_resume_end changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000500 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_resume_noirq
- Explanation: dpm_resume_noirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000501 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_resume_start
- Explanation: dpm_resume_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000503 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_suspend_end
- Explanation: dpm_suspend_end changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000504 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_suspend_late
- Explanation: dpm_suspend_late changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000505 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_suspend_noirq
- Explanation: dpm_suspend_noirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000506 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dpm_suspend_start
- Explanation: dpm_suspend_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000507 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drain_zonestat
- Explanation: drain_zonestat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000508 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_attach
- Explanation: driver_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000509 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_create_file
- Explanation: driver_create_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000510 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_deferred_probe_add
- Explanation: driver_deferred_probe_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000511 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_deferred_probe_check_state
- Explanation: driver_deferred_probe_check_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000513 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_find_device
- Explanation: driver_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000514 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_for_each_device
- Explanation: driver_for_each_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000515 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_init
- Explanation: driver_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000516 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_probe_done
- Explanation: driver_probe_done changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000517 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_register
- Explanation: driver_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000518 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_remove_file
- Explanation: driver_remove_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000519 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_set_override
- Explanation: driver_set_override changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000520 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: driver_unregister
- Explanation: driver_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000521 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drop_caches_sysctl_handler
- Explanation: drop_caches_sysctl_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000522 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drop_slab
- Explanation: drop_slab changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000523 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dst_pending_confirm
- Explanation: dst_pending_confirm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000524 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_init
- Explanation: early_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000526 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_ioremap_init
- Explanation: early_ioremap_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000527 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_ioremap_reset
- Explanation: early_ioremap_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000528 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_ioremap_setup
- Explanation: early_ioremap_setup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000529 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_iounmap
- Explanation: early_iounmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000531 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_memremap_pgprot_adjust
- Explanation: early_memremap_pgprot_adjust changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000532 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_memremap_prot
- Explanation: early_memremap_prot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000533 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_memremap_ro
- Explanation: early_memremap_ro changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000534 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_memunmap
- Explanation: early_memunmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000535 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_pfn_to_nid
- Explanation: early_pfn_to_nid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000536 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: early_security_init
- Explanation: early_security_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000537 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: encap_hdr_csum
- Explanation: encap_hdr_csum changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000538 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: encapsulation
- Explanation: encapsulation changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000539 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: eth_header_parse
- Explanation: eth_header_parse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000540 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_check_ops
- Explanation: ethtool_check_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000541 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_convert_legacy_u32_to_link_mode
- Explanation: ethtool_convert_legacy_u32_to_link_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000542 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_convert_link_mode_to_legacy_u32
- Explanation: ethtool_convert_link_mode_to_legacy_u32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000543 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_forced_speed_maps_init
- Explanation: ethtool_forced_speed_maps_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000544 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_get_phc_vclocks
- Explanation: ethtool_get_phc_vclocks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000545 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_get_ts_info_by_layer
- Explanation: ethtool_get_ts_info_by_layer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000546 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_intersect_link_masks
- Explanation: ethtool_intersect_link_masks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000547 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_op_get_link
- Explanation: ethtool_op_get_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000548 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_op_get_ts_info
- Explanation: ethtool_op_get_ts_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000549 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_params_from_link_mode
- Explanation: ethtool_params_from_link_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000550 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_puts
- Explanation: ethtool_puts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000551 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_rx_flow_rule_create
- Explanation: ethtool_rx_flow_rule_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000552 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_rx_flow_rule_destroy
- Explanation: ethtool_rx_flow_rule_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000553 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_set_ethtool_phy_ops
- Explanation: ethtool_set_ethtool_phy_ops changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000554 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_sprintf
- Explanation: ethtool_sprintf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000555 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_virtdev_set_link_ksettings
- Explanation: ethtool_virtdev_set_link_ksettings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000556 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_virtdev_validate_cmd
- Explanation: ethtool_virtdev_validate_cmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000557 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exact_match
- Explanation: exact_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000558 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exec_task_namespaces
- Explanation: exec_task_namespaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000559 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_mmap
- Explanation: exit_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000560 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: exit_task_namespaces
- Explanation: exit_task_namespaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000561 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: expand_downwards
- Explanation: expand_downwards changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000563 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: expand_stack_locked
- Explanation: expand_stack_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000565 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fclone
- Explanation: fclone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000566 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fd_install
- Explanation: fd_install changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000568 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fget_raw
- Explanation: fget_raw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000569 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fget_task
- Explanation: fget_task changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000570 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_fault
- Explanation: filemap_fault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000571 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_map_pages
- Explanation: filemap_map_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000572 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filemap_page_mkwrite
- Explanation: filemap_page_mkwrite changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000573 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filter_irq_stacks
- Explanation: filter_irq_stacks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000574 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_extend_vma_locked
- Explanation: find_extend_vma_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000575 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_io_range_by_fwnode
- Explanation: find_io_range_by_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000576 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_mergeable_anon_vma
- Explanation: find_mergeable_anon_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000577 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_vm_area
- Explanation: find_vm_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000579 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_vma_intersection
- Explanation: find_vma_intersection changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000580 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_vma_prev
- Explanation: find_vma_prev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000581 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: find_vmap_area
- Explanation: find_vmap_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000582 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: finish_fault
- Explanation: finish_fault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000583 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fixup_user_fault
- Explanation: fixup_user_fault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000584 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flow_get_u32_dst
- Explanation: flow_get_u32_dst changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000585 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flow_get_u32_src
- Explanation: flow_get_u32_src changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000586 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flow_hash_from_keys
- Explanation: flow_hash_from_keys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000587 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: flush_delayed_fput
- Explanation: flush_delayed_fput changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000589 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fold_vm_numa_events
- Explanation: fold_vm_numa_events changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000590 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_add_pin
- Explanation: folio_add_pin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000591 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_copy
- Explanation: folio_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000592 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_mark_dirty
- Explanation: folio_mark_dirty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000593 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: folio_total_mapcount
- Explanation: folio_total_mapcount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000594 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: follow_page
- Explanation: follow_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000595 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: follow_pfn
- Explanation: follow_pfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000596 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: follow_phys
- Explanation: follow_phys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000597 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: follow_pte
- Explanation: follow_pte changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000598 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: force_media
- Explanation: force_media changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000599 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fput
- Explanation: fput changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000600 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_area_init
- Explanation: free_area_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000601 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_initmem
- Explanation: free_initmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000602 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_nsproxy
- Explanation: free_nsproxy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000603 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_pgd_range
- Explanation: free_pgd_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000604 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_reserved_area
- Explanation: free_reserved_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000605 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_sched_domains
- Explanation: free_sched_domains changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000606 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: free_vm_area
- Explanation: free_vm_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000607 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: full_duplex
- Explanation: full_duplex changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000608 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fw_devlink_is_strict
- Explanation: fw_devlink_is_strict changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000609 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fw_devlink_purge_absent_suppliers
- Explanation: fw_devlink_purge_absent_suppliers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000610 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_phy_id
- Explanation: fwnode_get_phy_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000612 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_link_add
- Explanation: fwnode_link_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000613 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_links_purge
- Explanation: fwnode_links_purge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000614 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_mdio_find_device
- Explanation: fwnode_mdio_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000616 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gen10g_config_aneg
- Explanation: gen10g_config_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000617 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_access_phys
- Explanation: generic_access_phys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000619 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_error_remove_folio
- Explanation: generic_error_remove_folio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000620 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_mii_ioctl
- Explanation: generic_mii_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000621 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_aneg_done
- Explanation: genphy_aneg_done changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000622 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c37_config_aneg
- Explanation: genphy_c37_config_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000623 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c37_read_status
- Explanation: genphy_c37_read_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000624 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_an_config_aneg
- Explanation: genphy_c45_an_config_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000625 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_an_config_eee_aneg
- Explanation: genphy_c45_an_config_eee_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000626 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_an_disable_aneg
- Explanation: genphy_c45_an_disable_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000627 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_aneg_done
- Explanation: genphy_c45_aneg_done changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000628 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_baset1_read_status
- Explanation: genphy_c45_baset1_read_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000629 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_check_and_restart_aneg
- Explanation: genphy_c45_check_and_restart_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000630 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_config_aneg
- Explanation: genphy_c45_config_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000631 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_eee_is_active
- Explanation: genphy_c45_eee_is_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000632 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_ethtool_get_eee
- Explanation: genphy_c45_ethtool_get_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000633 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_ethtool_set_eee
- Explanation: genphy_c45_ethtool_set_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000634 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_fast_retrain
- Explanation: genphy_c45_fast_retrain changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000635 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_loopback
- Explanation: genphy_c45_loopback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000636 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_plca_get_cfg
- Explanation: genphy_c45_plca_get_cfg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000637 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_plca_get_status
- Explanation: genphy_c45_plca_get_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000638 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_plca_set_cfg
- Explanation: genphy_c45_plca_set_cfg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000639 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_pma_baset1_read_abilities
- Explanation: genphy_c45_pma_baset1_read_abilities changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000640 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_pma_baset1_read_master_slave
- Explanation: genphy_c45_pma_baset1_read_master_slave changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000641 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_pma_baset1_setup_master_slave
- Explanation: genphy_c45_pma_baset1_setup_master_slave changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000642 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_pma_read_abilities
- Explanation: genphy_c45_pma_read_abilities changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000643 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_pma_read_ext_abilities
- Explanation: genphy_c45_pma_read_ext_abilities changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000644 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_pma_resume
- Explanation: genphy_c45_pma_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000645 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_pma_setup_forced
- Explanation: genphy_c45_pma_setup_forced changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000646 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_pma_suspend
- Explanation: genphy_c45_pma_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000647 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_read_eee_abilities
- Explanation: genphy_c45_read_eee_abilities changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000648 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_read_eee_adv
- Explanation: genphy_c45_read_eee_adv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000649 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_read_link
- Explanation: genphy_c45_read_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000650 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_read_lpa
- Explanation: genphy_c45_read_lpa changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000651 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_read_mdix
- Explanation: genphy_c45_read_mdix changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000652 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_read_pma
- Explanation: genphy_c45_read_pma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000653 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_read_status
- Explanation: genphy_c45_read_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000654 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_restart_aneg
- Explanation: genphy_c45_restart_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000655 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_c45_write_eee_adv
- Explanation: genphy_c45_write_eee_adv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000656 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_check_and_restart_aneg
- Explanation: genphy_check_and_restart_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000657 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_config_eee_advert
- Explanation: genphy_config_eee_advert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000658 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_handle_interrupt_no_ack
- Explanation: genphy_handle_interrupt_no_ack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000659 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_loopback
- Explanation: genphy_loopback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000662 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_read_master_slave
- Explanation: genphy_read_master_slave changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000663 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_read_mmd_unsupported
- Explanation: genphy_read_mmd_unsupported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000665 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_read_status_fixed
- Explanation: genphy_read_status_fixed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000666 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_restart_aneg
- Explanation: genphy_restart_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000668 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_setup_forced
- Explanation: genphy_setup_forced changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000672 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_write_mmd_unsupported
- Explanation: genphy_write_mmd_unsupported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000674 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_close_on_exec
- Explanation: get_close_on_exec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000675 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_cmdline
- Explanation: get_cmdline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000676 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_compat_msghdr
- Explanation: get_compat_msghdr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000678 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_dump_page
- Explanation: get_dump_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000679 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_gate_vma
- Explanation: get_gate_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000680 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_mm_exe_file
- Explanation: get_mm_exe_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000681 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_pfn_range_for_nid
- Explanation: get_pfn_range_for_nid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000684 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_task_exe_file
- Explanation: get_task_exe_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000685 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_unmapped_area
- Explanation: get_unmapped_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000686 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_unused_fd_flags
- Explanation: get_unused_fd_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000689 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_user_pages_fast_only
- Explanation: get_user_pages_fast_only changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000690 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_user_pages_remote
- Explanation: get_user_pages_remote changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000691 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_user_pages_unlocked
- Explanation: get_user_pages_unlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000693 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_vm_area_caller
- Explanation: get_vm_area_caller changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000694 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gpio_led_register_device
- Explanation: gpio_led_register_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000695 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: handle_mm_fault
- Explanation: handle_mm_fault changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000696 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: has_fixups
- Explanation: has_fixups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000697 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: head_frag
- Explanation: head_frag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000698 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hsiphash_1u32
- Explanation: hsiphash_1u32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000699 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hsiphash_2u32
- Explanation: hsiphash_2u32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000700 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hsiphash_3u32
- Explanation: hsiphash_3u32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000701 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: hsiphash_4u32
- Explanation: hsiphash_4u32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000702 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: huge_pmd_set_accessed
- Explanation: huge_pmd_set_accessed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000703 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: huge_pud_set_accessed
- Explanation: huge_pud_set_accessed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000704 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: idle_notification
- Explanation: idle_notification changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000705 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ignore_children
- Explanation: ignore_children changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000706 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ignore_df
- Explanation: ignore_df changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000709 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: in_dpm_list
- Explanation: in_dpm_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000711 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: in_gate_area_no_mm
- Explanation: in_gate_area_no_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000712 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inc_node_page_state
- Explanation: inc_node_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000713 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inc_node_state
- Explanation: inc_node_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000714 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inc_zone_page_state
- Explanation: inc_zone_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000715 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inet_proto_csum_replace16
- Explanation: inet_proto_csum_replace16 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000716 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inet_proto_csum_replace4
- Explanation: inet_proto_csum_replace4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000717 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inet_proto_csum_replace_by_diff
- Explanation: inet_proto_csum_replace_by_diff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000718 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: init_mm_internals
- Explanation: init_mm_internals changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000719 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inner_protocol_type
- Explanation: inner_protocol_type changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000721 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: insert_resource_conflict
- Explanation: insert_resource_conflict changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000722 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: insert_resource_expand_to_fit
- Explanation: insert_resource_expand_to_fit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000723 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: insert_vm_struct
- Explanation: insert_vm_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000724 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: install_special_mapping
- Explanation: install_special_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000725 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: interrupts
- Explanation: interrupts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000726 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: io_delay_init
- Explanation: io_delay_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000727 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iomem_get_mapping
- Explanation: iomem_get_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000728 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iomem_is_exclusive
- Explanation: iomem_is_exclusive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000729 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iomem_map_sanity_check
- Explanation: iomem_map_sanity_check changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000730 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioport_map
- Explanation: ioport_map changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000731 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioport_unmap
- Explanation: ioport_unmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000733 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioread16_rep
- Explanation: ioread16_rep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000734 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioread16be
- Explanation: ioread16be changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000736 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioread32_rep
- Explanation: ioread32_rep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000737 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioread32be
- Explanation: ioread32be changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000739 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioread64_hi_lo
- Explanation: ioread64_hi_lo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000740 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioread64_lo_hi
- Explanation: ioread64_lo_hi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000742 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioread64be_hi_lo
- Explanation: ioread64be_hi_lo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000743 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioread64be_lo_hi
- Explanation: ioread64be_lo_hi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000745 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioread8_rep
- Explanation: ioread8_rep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000747 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioremap_cache
- Explanation: ioremap_cache changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000748 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioremap_change_attr
- Explanation: ioremap_change_attr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000749 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioremap_encrypted
- Explanation: ioremap_encrypted changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000750 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioremap_page_range
- Explanation: ioremap_page_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000751 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioremap_prot
- Explanation: ioremap_prot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000752 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioremap_uc
- Explanation: ioremap_uc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000753 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioremap_wc
- Explanation: ioremap_wc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000754 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ioremap_wt
- Explanation: ioremap_wt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000755 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iounmap
- Explanation: iounmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000757 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iowrite16_rep
- Explanation: iowrite16_rep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000758 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iowrite16be
- Explanation: iowrite16be changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000760 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iowrite32_rep
- Explanation: iowrite32_rep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000761 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iowrite32be
- Explanation: iowrite32be changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000763 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iowrite64_hi_lo
- Explanation: iowrite64_hi_lo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000764 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iowrite64_lo_hi
- Explanation: iowrite64_lo_hi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000766 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iowrite64be_hi_lo
- Explanation: iowrite64be_hi_lo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000767 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iowrite64be_lo_hi
- Explanation: iowrite64be_lo_hi changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000769 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: iowrite8_rep
- Explanation: iowrite8_rep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000770 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ip_compute_csum
- Explanation: ip_compute_csum changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000771 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ip_summed
- Explanation: ip_summed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000773 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_enter_rcu
- Explanation: irq_enter_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000775 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_exit_rcu
- Explanation: irq_exit_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000776 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_rerun
- Explanation: irq_rerun changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000777 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_safe
- Explanation: irq_safe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000778 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: irq_suspended
- Explanation: irq_suspended changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000779 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_c45
- Explanation: is_c45 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000780 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_early_ioremap_ptep
- Explanation: is_early_ioremap_ptep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000781 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_gigabit_capable
- Explanation: is_gigabit_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000782 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_internal
- Explanation: is_internal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000784 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_late_suspended
- Explanation: is_late_suspended changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000785 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_noirq_suspended
- Explanation: is_noirq_suspended changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000786 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_on_sfp_module
- Explanation: is_on_sfp_module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000787 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_prepared
- Explanation: is_prepared changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000788 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_pseudo_fixed_link
- Explanation: is_pseudo_fixed_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000789 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_suspended
- Explanation: is_suspended changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000790 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_vmalloc_addr
- Explanation: is_vmalloc_addr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000791 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: is_vmalloc_or_module_addr
- Explanation: is_vmalloc_or_module_addr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000792 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_accept
- Explanation: kernel_accept changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000793 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_bind
- Explanation: kernel_bind changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000794 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_connect
- Explanation: kernel_connect changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000795 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_getpeername
- Explanation: kernel_getpeername changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000796 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_getsockname
- Explanation: kernel_getsockname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000797 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_listen
- Explanation: kernel_listen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000799 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_read_file_from_fd
- Explanation: kernel_read_file_from_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000801 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_read_file_from_path_initns
- Explanation: kernel_read_file_from_path_initns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000802 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_recvmsg
- Explanation: kernel_recvmsg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000804 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_sendmsg_locked
- Explanation: kernel_sendmsg_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000805 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_sock_ip_overhead
- Explanation: kernel_sock_ip_overhead changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000806 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kernel_sock_shutdown
- Explanation: kernel_sock_shutdown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000807 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kfree_skb_list_reason
- Explanation: kfree_skb_list_reason changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000808 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kfree_skb_partial
- Explanation: kfree_skb_partial changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000809 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kfree_skb_reason
- Explanation: kfree_skb_reason changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000810 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kill_device
- Explanation: kill_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000811 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: klist_add_before
- Explanation: klist_add_before changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000812 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: klist_add_behind
- Explanation: klist_add_behind changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000813 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: klist_add_head
- Explanation: klist_add_head changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000814 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: klist_add_tail
- Explanation: klist_add_tail changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000815 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: klist_del
- Explanation: klist_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000816 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: klist_init
- Explanation: klist_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000817 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: klist_iter_exit
- Explanation: klist_iter_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000819 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: klist_iter_init_node
- Explanation: klist_iter_init_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000820 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: klist_next
- Explanation: klist_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000821 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: klist_node_attached
- Explanation: klist_node_attached changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000822 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: klist_prev
- Explanation: klist_prev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000823 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: klist_remove
- Explanation: klist_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000824 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: kunit_merge_suite_sets
- Explanation: kunit_merge_suite_sets changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000825 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: l4_hash
- Explanation: l4_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000826 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_add_lookup
- Explanation: led_add_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000828 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_blink_set_nosleep
- Explanation: led_blink_set_nosleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000829 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_blink_set_oneshot
- Explanation: led_blink_set_oneshot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000830 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_classdev_register_ext
- Explanation: led_classdev_register_ext changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000831 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_classdev_resume
- Explanation: led_classdev_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000832 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_classdev_suspend
- Explanation: led_classdev_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000833 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_classdev_unregister
- Explanation: led_classdev_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000834 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_compose_name
- Explanation: led_compose_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000836 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_get_default_pattern
- Explanation: led_get_default_pattern changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000837 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_init_default_state_get
- Explanation: led_init_default_state_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000838 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_put
- Explanation: led_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000839 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_remove_lookup
- Explanation: led_remove_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000841 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_set_brightness_sync
- Explanation: led_set_brightness_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000842 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_sysfs_disable
- Explanation: led_sysfs_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000843 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_sysfs_enable
- Explanation: led_sysfs_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000845 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_trigger_blink_oneshot
- Explanation: led_trigger_blink_oneshot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000846 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_trigger_event
- Explanation: led_trigger_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000848 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_trigger_register_simple
- Explanation: led_trigger_register_simple changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000849 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_trigger_remove
- Explanation: led_trigger_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000851 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_trigger_set_default
- Explanation: led_trigger_set_default changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000853 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_trigger_unregister_simple
- Explanation: led_trigger_unregister_simple changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000854 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: led_update_brightness
- Explanation: led_update_brightness changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000857 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: linkmode_resolve_pause
- Explanation: linkmode_resolve_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000858 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: linkmode_set_pause
- Explanation: linkmode_set_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000860 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: list_lru_add_obj
- Explanation: list_lru_add_obj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000862 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: list_lru_del_obj
- Explanation: list_lru_del_obj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000863 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: list_lru_putback
- Explanation: list_lru_putback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000865 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lock_device_hotplug_sysfs
- Explanation: lock_device_hotplug_sysfs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000866 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lock_mm_and_find_vma
- Explanation: lock_mm_and_find_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000867 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lock_vma_under_rcu
- Explanation: lock_vma_under_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000868 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: logic_pio_register_range
- Explanation: logic_pio_register_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000869 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: logic_pio_to_hwaddr
- Explanation: logic_pio_to_hwaddr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000870 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: logic_pio_trans_cpuaddr
- Explanation: logic_pio_trans_cpuaddr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000871 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: logic_pio_trans_hwaddr
- Explanation: logic_pio_trans_hwaddr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000872 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: logic_pio_unregister_range
- Explanation: logic_pio_unregister_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000874 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lookup_resource
- Explanation: lookup_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000875 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: loopback_enabled
- Explanation: loopback_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000876 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lsm_fill_user_ctx
- Explanation: lsm_fill_user_ctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000877 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: lsm_name_to_attr
- Explanation: lsm_name_to_attr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000878 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mac_managed_pm
- Explanation: mac_managed_pm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000879 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: madvise_free_huge_pmd
- Explanation: madvise_free_huge_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000880 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: make_flow_keys_digest
- Explanation: make_flow_keys_digest changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000884 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: may_expand_vm
- Explanation: may_expand_vm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000885 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: may_skip_resume
- Explanation: may_skip_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000886 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio45_ethtool_gset_npage
- Explanation: mdio45_ethtool_gset_npage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000887 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio45_ethtool_ksettings_get_npage
- Explanation: mdio45_ethtool_ksettings_get_npage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000888 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio45_links_ok
- Explanation: mdio45_links_ok changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000889 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio45_nway_restart
- Explanation: mdio45_nway_restart changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000890 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio45_probe
- Explanation: mdio45_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000891 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_bus_exit
- Explanation: mdio_bus_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000892 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_bus_init
- Explanation: mdio_bus_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000893 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_device_bus_match
- Explanation: mdio_device_bus_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000894 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_device_create
- Explanation: mdio_device_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000895 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_device_free
- Explanation: mdio_device_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000896 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_device_register
- Explanation: mdio_device_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000897 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_device_remove
- Explanation: mdio_device_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000898 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_device_reset
- Explanation: mdio_device_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000899 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_driver_register
- Explanation: mdio_driver_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000900 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_driver_unregister
- Explanation: mdio_driver_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000901 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_find_bus
- Explanation: mdio_find_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000902 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_mii_ioctl
- Explanation: mdio_mii_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000903 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdio_set_flag
- Explanation: mdio_set_flag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000904 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_alloc_size
- Explanation: mdiobus_alloc_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000906 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_c45_modify_changed
- Explanation: mdiobus_c45_modify_changed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000908 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_c45_read_nested
- Explanation: mdiobus_c45_read_nested changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000910 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_c45_write_nested
- Explanation: mdiobus_c45_write_nested changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000911 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_free
- Explanation: mdiobus_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000912 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_get_phy
- Explanation: mdiobus_get_phy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000913 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_is_registered_device
- Explanation: mdiobus_is_registered_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000915 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_modify_changed
- Explanation: mdiobus_modify_changed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000917 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_read_nested
- Explanation: mdiobus_read_nested changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000918 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_register_board_info
- Explanation: mdiobus_register_board_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000919 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_register_device
- Explanation: mdiobus_register_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000920 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_scan_c22
- Explanation: mdiobus_scan_c22 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000922 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_unregister_device
- Explanation: mdiobus_unregister_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000924 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_write_nested
- Explanation: mdiobus_write_nested changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000925 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mem_dump_obj
- Explanation: mem_dump_obj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000926 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mem_init
- Explanation: mem_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000927 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memalloc_noio
- Explanation: memalloc_noio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000928 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memcmp_pages
- Explanation: memcmp_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000929 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memcpy_fromio
- Explanation: memcpy_fromio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000930 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memcpy_toio
- Explanation: memcpy_toio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000931 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memory_add_physaddr_to_nid
- Explanation: memory_add_physaddr_to_nid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000933 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memory_failure_queue_kick
- Explanation: memory_failure_queue_kick changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000935 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memset_io
- Explanation: memset_io changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000936 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: memunmap
- Explanation: memunmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000937 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mf_dax_kill_procs
- Explanation: mf_dax_kill_procs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000938 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mii_check_gmii_support
- Explanation: mii_check_gmii_support changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000939 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mii_check_link
- Explanation: mii_check_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000940 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mii_check_media
- Explanation: mii_check_media changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000941 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mii_ethtool_get_link_ksettings
- Explanation: mii_ethtool_get_link_ksettings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000942 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mii_ethtool_gset
- Explanation: mii_ethtool_gset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000943 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mii_ethtool_set_link_ksettings
- Explanation: mii_ethtool_set_link_ksettings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000944 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mii_ethtool_sset
- Explanation: mii_ethtool_sset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000945 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mii_link_ok
- Explanation: mii_link_ok changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000946 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mii_nway_restart
- Explanation: mii_nway_restart changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000947 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_account_pinned_pages
- Explanation: mm_account_pinned_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000948 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_core_init
- Explanation: mm_core_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000949 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_drop_all_locks
- Explanation: mm_drop_all_locks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000950 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_take_all_locks
- Explanation: mm_take_all_locks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000951 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_trace_rss_stat
- Explanation: mm_trace_rss_stat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000952 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mm_unaccount_pinned_pages
- Explanation: mm_unaccount_pinned_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000953 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_init
- Explanation: mmap_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000954 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_min_addr_handler
- Explanation: mmap_min_addr_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000955 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_region
- Explanation: mmap_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000956 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mod_node_page_state
- Explanation: mod_node_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000957 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mod_zone_page_state
- Explanation: mod_zone_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000959 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mono_delivery_time
- Explanation: mono_delivery_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000960 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: move_huge_pmd
- Explanation: move_huge_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000961 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: move_page_tables
- Explanation: move_page_tables changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000962 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mpls_bos
- Explanation: mpls_bos changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000963 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mpls_label
- Explanation: mpls_label changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000964 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mpls_tc
- Explanation: mpls_tc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000965 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mpls_ttl
- Explanation: mpls_ttl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000966 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mprotect_fixup
- Explanation: mprotect_fixup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000967 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msg_zerocopy_callback
- Explanation: msg_zerocopy_callback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000968 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msg_zerocopy_put_abort
- Explanation: msg_zerocopy_put_abort changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000969 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msg_zerocopy_realloc
- Explanation: msg_zerocopy_realloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000971 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msleep_interruptible
- Explanation: msleep_interruptible changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000972 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mtree_dup
- Explanation: mtree_dup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000973 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: must_resume
- Explanation: must_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000974 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: napi_build_skb
- Explanation: napi_build_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000975 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: napi_consume_skb
- Explanation: napi_consume_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000976 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: napi_pp_put_page
- Explanation: napi_pp_put_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000977 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: napi_skb_free_stolen_head
- Explanation: napi_skb_free_stolen_head changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000978 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: native_io_delay
- Explanation: native_io_delay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000979 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ndisc_nodetype
- Explanation: ndisc_nodetype changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000980 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: needs_force_resume
- Explanation: needs_force_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000981 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: net_ratelimit
- Explanation: net_ratelimit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000982 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netdev_alert
- Explanation: netdev_alert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000983 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netdev_crit
- Explanation: netdev_crit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000984 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netdev_emerg
- Explanation: netdev_emerg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000985 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netdev_err
- Explanation: netdev_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000986 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netdev_info
- Explanation: netdev_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000987 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netdev_notice
- Explanation: netdev_notice changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000988 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netdev_printk
- Explanation: netdev_printk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000989 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netdev_warn
- Explanation: netdev_warn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000990 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_ack
- Explanation: netlink_ack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000991 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_add_tap
- Explanation: netlink_add_tap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000992 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_alloc_large_skb
- Explanation: netlink_alloc_large_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000993 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_attachskb
- Explanation: netlink_attachskb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000995 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_broadcast_filtered
- Explanation: netlink_broadcast_filtered changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000996 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_capable
- Explanation: netlink_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000997 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_change_ngroups
- Explanation: netlink_change_ngroups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000998 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_detachskb
- Explanation: netlink_detachskb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000999 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_getsockbyfilp
- Explanation: netlink_getsockbyfilp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001000 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_has_listeners
- Explanation: netlink_has_listeners changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001001 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_kernel_release
- Explanation: netlink_kernel_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001002 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_net_capable
- Explanation: netlink_net_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_ns_capable
- Explanation: netlink_ns_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_register_notifier
- Explanation: netlink_register_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001005 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_remove_tap
- Explanation: netlink_remove_tap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001006 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_sendskb
- Explanation: netlink_sendskb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_set_err
- Explanation: netlink_set_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_strict_get_check
- Explanation: netlink_strict_get_check changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_table_grab
- Explanation: netlink_table_grab changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_table_ungrab
- Explanation: netlink_table_ungrab changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001011 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_unicast
- Explanation: netlink_unicast changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001012 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: netlink_unregister_notifier
- Explanation: netlink_unregister_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_1
- Explanation: new_bitfield_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'lineno', 'type': 'core::ffi::c_uint'}, {'name': 'class_id', 'type': 'core::ffi::c_uint'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'is_c45', 'type': 'core::ffi::c_uint'}, {'name': 'is_internal', 'type': 'core::ffi::c_uint'}, {'name': 'is_pseudo_fixed_link', 'type': 'core::ffi::c_uint'}, {'name': 'is_gigabit_capable', 'type': 'core::ffi::c_uint'}, {'name': 'has_fixups', 'type': 'core::ffi::c_uint'}, {'name': 'suspended', 'type': 'core::ffi::c_uint'}, {'name': 'suspended_by_mdio_bus', 'type': 'core::ffi::c_uint'}, {'name': 'sysfs_links', 'type': 'core::ffi::c_uint'}, {'name': 'loopback_enabled', 'type': 'core::ffi::c_uint'}, {'name': 'downshifted_rate', 'type': 'core::ffi::c_uint'}, {'name': 'is_on_sfp_module', 'type': 'core::ffi::c_uint'}, {'name': 'mac_managed_pm', 'type': 'core::ffi::c_uint'}, {'name': 'wol_enabled', 'type': 'core::ffi::c_uint'}, {'name': 'autoneg', 'type': 'core::ffi::c_uint'}, {'name': 'link', 'type': 'core::ffi::c_uint'}, {'name': 'autoneg_complete', 'type': 'core::ffi::c_uint'}, {'name': 'interrupts', 'type': 'core::ffi::c_uint'}, {'name': 'irq_suspended', 'type': 'core::ffi::c_uint'}, {'name': 'irq_rerun', 'type': 'core::ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-001014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_2
- Explanation: new_bitfield_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'mce_ripv', 'type': '__u64'}, {'name': 'mce_whole_page', 'type': '__u64'}, {'name': '__mce_reserved', 'type': '__u64'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'mono_delivery_time', 'type': '__u8'}, {'name': 'tc_at_ingress', 'type': '__u8'}, {'name': 'tc_skip_classify', 'type': '__u8'}, {'name': 'remcsum_offload', 'type': '__u8'}, {'name': 'csum_complete_sw', 'type': '__u8'}, {'name': 'csum_level', 'type': '__u8'}, {'name': 'inner_protocol_type', 'type': '__u8'}, {'name': 'l4_hash', 'type': '__u8'}, {'name': 'sw_hash', 'type': '__u8'}, {'name': 'wifi_acked_valid', 'type': '__u8'}, {'name': 'wifi_acked', 'type': '__u8'}, {'name': 'no_fcs', 'type': '__u8'}, {'name': 'encapsulation', 'type': '__u8'}, {'name': 'encap_hdr_csum', 'type': '__u8'}, {'name': 'csum_valid', 'type': '__u8'}, {'name': 'ndisc_nodetype', 'type': '__u8'}, {'name': 'redirected', 'type': '__u8'}, {'name': 'nf_skip_egress', 'type': '__u8'}, {'name': 'slow_gro', 'type': '__u8'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-001015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: new_bitfield_3
- Explanation: new_bitfield_3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': '__BindgenBitfieldUnit<[u8'}`
- New: `{'params': [{'name': 'disable_depth', 'type': 'core::ffi::c_uint'}, {'name': 'idle_notification', 'type': 'core::ffi::c_uint'}, {'name': 'request_pending', 'type': 'core::ffi::c_uint'}, {'name': 'deferred_resume', 'type': 'core::ffi::c_uint'}, {'name': 'needs_force_resume', 'type': 'core::ffi::c_uint'}, {'name': 'runtime_auto', 'type': 'core::ffi::c_uint'}, {'name': 'ignore_children', 'type': 'bool_'}, {'name': 'no_callbacks', 'type': 'core::ffi::c_uint'}, {'name': 'irq_safe', 'type': 'core::ffi::c_uint'}, {'name': 'use_autosuspend', 'type': 'core::ffi::c_uint'}, {'name': 'timer_autosuspends', 'type': 'core::ffi::c_uint'}, {'name': 'memalloc_noio', 'type': 'core::ffi::c_uint'}], 'return_type': '__BindgenBitfieldUnit<[u8'}`

### Rust Evidence

- Graph edges: `1`

## W-001016 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nf_conntrack_destroy
- Explanation: nf_conntrack_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nf_skip_egress
- Explanation: nf_skip_egress changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_callbacks
- Explanation: no_callbacks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_fcs
- Explanation: no_fcs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001021 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: no_pm_callbacks
- Explanation: no_pm_callbacks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: node_map_pfn_alignment
- Explanation: node_map_pfn_alignment changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001024 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: node_page_state_pages
- Explanation: node_page_state_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nohdr
- Explanation: nohdr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nommu_shrink_inode_mappings
- Explanation: nommu_shrink_inode_mappings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001027 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nop_func
- Explanation: nop_func changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nr_free_buffer_pages
- Explanation: nr_free_buffer_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: nsproxy_cache_init
- Explanation: nsproxy_cache_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001030 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: of_led_get
- Explanation: of_led_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: of_node_reused
- Explanation: of_node_reused changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: of_set_phy_eee_broken
- Explanation: of_set_phy_eee_broken changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: of_set_phy_supported
- Explanation: of_set_phy_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: offline_disabled
- Explanation: offline_disabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: online
- Explanation: online changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ooo_okay
- Explanation: ooo_okay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001038 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: overcommit_kbytes_handler
- Explanation: overcommit_kbytes_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: overcommit_policy_handler
- Explanation: overcommit_policy_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001040 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: overcommit_ratio_handler
- Explanation: overcommit_ratio_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: p4d_clear_bad
- Explanation: p4d_clear_bad changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: p4d_clear_huge
- Explanation: p4d_clear_huge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001043 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: p4d_free_pud_page
- Explanation: p4d_free_pud_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001044 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: p4d_set_huge
- Explanation: p4d_set_huge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001045 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: page_is_ram
- Explanation: page_is_ram changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001046 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pagecache_init
- Explanation: pagecache_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pagecache_isize_extended
- Explanation: pagecache_isize_extended changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pagefault_out_of_memory
- Explanation: pagefault_out_of_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001049 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: panic_indicator
- Explanation: panic_indicator changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: paravirt_patch
- Explanation: paravirt_patch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-001052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: parse_args
- Explanation: parse_args changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'args', 'type': '*mut core::ffi::c_char'}, {'name': 'params', 'type': '*const kernel_param'}, {'name': 'num', 'type': 'core::ffi::c_uint'}, {'name': 'level_min', 'type': 's16'}, {'name': 'level_max', 'type': 's16'}, {'name': 'arg', 'type': '*mut core::ffi::c_void'}, {'name': 'unknown', 'type': '::core::option::Option< unsafe extern "C" fn( param: *mut core::ffi::c_char, val: *mut core::ffi::c_char, doing: *const core::ffi::c_char, arg: *mut core::ffi::c_void,'}], 'return_type': 'core::ffi::c_int, >, ) -> *mut core::ffi::c_char'}`
- New: `{'params': [{'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'args', 'type': '*mut core::ffi::c_char'}, {'name': 'params', 'type': '*const kernel_param'}, {'name': 'num', 'type': 'core::ffi::c_uint'}, {'name': 'level_min', 'type': 's16'}, {'name': 'level_max', 'type': 's16'}, {'name': 'arg', 'type': '*mut core::ffi::c_void'}, {'name': 'unknown', 'type': 'parse_unknown_fn'}], 'return_type': '*mut core::ffi::c_char'}`

### Rust Evidence

- Graph edges: `1`

## W-001054 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: partition_sched_domains_locked
- Explanation: partition_sched_domains_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001056 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_iomap_range
- Explanation: pci_iomap_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001058 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_iomap_wc_range
- Explanation: pci_iomap_wc_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001059 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_iounmap
- Explanation: pci_iounmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001060 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcpu_free_vm_areas
- Explanation: pcpu_free_vm_areas changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001061 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pcpu_get_vm_areas
- Explanation: pcpu_get_vm_areas changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001062 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: peeked
- Explanation: peeked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001063 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pfmemalloc
- Explanation: pfmemalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001064 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pgd_clear_bad
- Explanation: pgd_clear_bad changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001065 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pgtable_trans_huge_deposit
- Explanation: pgtable_trans_huge_deposit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001066 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pgtable_trans_huge_withdraw
- Explanation: pgtable_trans_huge_withdraw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001067 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_advertise_supported
- Explanation: phy_advertise_supported changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_aneg_done
- Explanation: phy_aneg_done changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_attach_direct
- Explanation: phy_attach_direct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_attached_info_irq
- Explanation: phy_attached_info_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001073 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_attached_print
- Explanation: phy_attached_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001074 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_check_downshift
- Explanation: phy_check_downshift changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001075 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_check_valid
- Explanation: phy_check_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001076 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_config_aneg
- Explanation: phy_config_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001078 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_connect_direct
- Explanation: phy_connect_direct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_detach
- Explanation: phy_detach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001080 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_device_create
- Explanation: phy_device_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001082 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_device_register
- Explanation: phy_device_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_device_remove
- Explanation: phy_device_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_disable_interrupts
- Explanation: phy_disable_interrupts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001085 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_disconnect
- Explanation: phy_disconnect changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001087 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_do_ioctl_running
- Explanation: phy_do_ioctl_running changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001089 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_driver_is_genphy_10g
- Explanation: phy_driver_is_genphy_10g changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_driver_register
- Explanation: phy_driver_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_driver_unregister
- Explanation: phy_driver_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_duplex_to_str
- Explanation: phy_duplex_to_str changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001095 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_error
- Explanation: phy_error changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_get_eee
- Explanation: phy_ethtool_get_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001097 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_get_link_ksettings
- Explanation: phy_ethtool_get_link_ksettings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_get_plca_cfg
- Explanation: phy_ethtool_get_plca_cfg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001099 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_get_plca_status
- Explanation: phy_ethtool_get_plca_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001100 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_get_sset_count
- Explanation: phy_ethtool_get_sset_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001101 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_get_stats
- Explanation: phy_ethtool_get_stats changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_get_strings
- Explanation: phy_ethtool_get_strings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001103 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_get_wol
- Explanation: phy_ethtool_get_wol changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001104 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_ksettings_get
- Explanation: phy_ethtool_ksettings_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_ksettings_set
- Explanation: phy_ethtool_ksettings_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_nway_reset
- Explanation: phy_ethtool_nway_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001107 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_set_eee
- Explanation: phy_ethtool_set_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001108 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_set_link_ksettings
- Explanation: phy_ethtool_set_link_ksettings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_set_plca_cfg
- Explanation: phy_ethtool_set_plca_cfg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_ethtool_set_wol
- Explanation: phy_ethtool_set_wol changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_find_first
- Explanation: phy_find_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001112 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_free_interrupt
- Explanation: phy_free_interrupt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001113 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_get_c45_ids
- Explanation: phy_get_c45_ids changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001114 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_get_eee_err
- Explanation: phy_get_eee_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001115 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_get_internal_delay
- Explanation: phy_get_internal_delay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_get_pause
- Explanation: phy_get_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001117 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_get_rate_matching
- Explanation: phy_get_rate_matching changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001118 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_init_eee
- Explanation: phy_init_eee changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001120 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_interface_num_ports
- Explanation: phy_interface_num_ports changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001121 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_lookup_setting
- Explanation: phy_lookup_setting changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001122 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_loopback
- Explanation: phy_loopback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001124 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_mii_ioctl
- Explanation: phy_mii_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001126 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_modify_changed
- Explanation: phy_modify_changed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_modify_mmd_changed
- Explanation: phy_modify_mmd_changed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001130 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_modify_paged_changed
- Explanation: phy_modify_paged_changed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001131 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_package_join
- Explanation: phy_package_join changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_package_leave
- Explanation: phy_package_leave changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_package_read_mmd
- Explanation: phy_package_read_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001134 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_package_write_mmd
- Explanation: phy_package_write_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_print_status
- Explanation: phy_print_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001136 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_queue_state_machine
- Explanation: phy_queue_state_machine changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_rate_matching_to_str
- Explanation: phy_rate_matching_to_str changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_read_mmd
- Explanation: phy_read_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001141 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_register_fixup_for_id
- Explanation: phy_register_fixup_for_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001142 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_register_fixup_for_uid
- Explanation: phy_register_fixup_for_uid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001143 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_remove_link_mode
- Explanation: phy_remove_link_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001144 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_request_interrupt
- Explanation: phy_request_interrupt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_reset_after_clk_enable
- Explanation: phy_reset_after_clk_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001147 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_resolve_aneg_pause
- Explanation: phy_resolve_aneg_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001148 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_resolve_pause
- Explanation: phy_resolve_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_restart_aneg
- Explanation: phy_restart_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_restore_page
- Explanation: phy_restore_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001151 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_resume
- Explanation: phy_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001152 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_save_page
- Explanation: phy_save_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001153 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_select_page
- Explanation: phy_select_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_set_asym_pause
- Explanation: phy_set_asym_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_set_max_speed
- Explanation: phy_set_max_speed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_set_sym_pause
- Explanation: phy_set_sym_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_sfp_attach
- Explanation: phy_sfp_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_sfp_detach
- Explanation: phy_sfp_detach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001159 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_sfp_probe
- Explanation: phy_sfp_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_speed_down_core
- Explanation: phy_speed_down_core changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_speed_to_str
- Explanation: phy_speed_to_str changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_speed_up
- Explanation: phy_speed_up changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_speeds
- Explanation: phy_speeds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001166 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_start_aneg
- Explanation: phy_start_aneg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_start_cable_test_tdr
- Explanation: phy_start_cable_test_tdr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001169 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_start_machine
- Explanation: phy_start_machine changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001170 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_state_machine
- Explanation: phy_state_machine changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_stop_machine
- Explanation: phy_stop_machine changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001173 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_support_asym_pause
- Explanation: phy_support_asym_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001174 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_support_sym_pause
- Explanation: phy_support_sym_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_supported_speeds
- Explanation: phy_supported_speeds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_suspend
- Explanation: phy_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001177 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_trigger_machine
- Explanation: phy_trigger_machine changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001179 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_unregister_fixup_for_id
- Explanation: phy_unregister_fixup_for_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001180 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_unregister_fixup_for_uid
- Explanation: phy_unregister_fixup_for_uid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_validate_pause
- Explanation: phy_validate_pause changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001182 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_write_mmd
- Explanation: phy_write_mmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_write_paged
- Explanation: phy_write_paged changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001186 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phys_mem_access_prot_allowed
- Explanation: phys_mem_access_prot_allowed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001187 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phys_to_target_node
- Explanation: phys_to_target_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pin_user_pages_fast
- Explanation: pin_user_pages_fast changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001190 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pin_user_pages_remote
- Explanation: pin_user_pages_remote changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001191 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pin_user_pages_unlocked
- Explanation: pin_user_pages_unlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001196 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_complete
- Explanation: pm_generic_complete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001198 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_freeze_late
- Explanation: pm_generic_freeze_late changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_freeze_noirq
- Explanation: pm_generic_freeze_noirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001201 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_poweroff_late
- Explanation: pm_generic_poweroff_late changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001202 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_poweroff_noirq
- Explanation: pm_generic_poweroff_noirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001203 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_prepare
- Explanation: pm_generic_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001205 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_restore_early
- Explanation: pm_generic_restore_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001206 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_restore_noirq
- Explanation: pm_generic_restore_noirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001208 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_resume_early
- Explanation: pm_generic_resume_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001209 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_resume_noirq
- Explanation: pm_generic_resume_noirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001211 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_suspend_late
- Explanation: pm_generic_suspend_late changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001212 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_suspend_noirq
- Explanation: pm_generic_suspend_noirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001214 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_thaw_early
- Explanation: pm_generic_thaw_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001215 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_generic_thaw_noirq
- Explanation: pm_generic_thaw_noirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001216 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_relax
- Explanation: pm_relax changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001217 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_stay_awake
- Explanation: pm_stay_awake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001218 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_vt_switch_required
- Explanation: pm_vt_switch_required changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001219 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_vt_switch_unregister
- Explanation: pm_vt_switch_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001220 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_wakeup_dev_event
- Explanation: pm_wakeup_dev_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001221 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_wakeup_ws_event
- Explanation: pm_wakeup_ws_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001222 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmd_clear_bad
- Explanation: pmd_clear_bad changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001223 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmd_clear_huge
- Explanation: pmd_clear_huge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001224 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmd_free_pte_page
- Explanation: pmd_free_pte_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmd_init
- Explanation: pmd_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001226 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmd_set_huge
- Explanation: pmd_set_huge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001227 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pmdp_huge_clear_flush
- Explanation: pmdp_huge_clear_flush changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001230 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pp_recycle
- Explanation: pp_recycle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001233 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: print_vma_addr
- Explanation: print_vma_addr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001235 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: process_shares_mm
- Explanation: process_shares_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001236 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pskb_expand_head
- Explanation: pskb_expand_head changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001237 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pskb_extract
- Explanation: pskb_extract changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001238 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pskb_put
- Explanation: pskb_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001239 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pskb_trim_rcsum_slow
- Explanation: pskb_trim_rcsum_slow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001240 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pte_free_defer
- Explanation: pte_free_defer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001241 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pte_offset_map_nolock
- Explanation: pte_offset_map_nolock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pud_clear_bad
- Explanation: pud_clear_bad changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pud_clear_huge
- Explanation: pud_clear_huge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001245 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pud_free_pmd_page
- Explanation: pud_free_pmd_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001246 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pud_init
- Explanation: pud_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001247 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pud_set_huge
- Explanation: pud_set_huge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001248 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pudp_huge_clear_flush
- Explanation: pudp_huge_clear_flush changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001249 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_cmsg_compat
- Explanation: put_cmsg_compat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001250 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_device
- Explanation: put_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001251 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_pages_list
- Explanation: put_pages_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001252 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_unused_fd
- Explanation: put_unused_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001253 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: quiet_vmstat
- Explanation: quiet_vmstat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001254 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: randomize_page
- Explanation: randomize_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001255 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: randomize_stack_top
- Explanation: randomize_stack_top changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001260 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: receive_fd_replace
- Explanation: receive_fd_replace changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001262 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: redirected
- Explanation: redirected changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001263 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: refresh_zone_stat_thresholds
- Explanation: refresh_zone_stat_thresholds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001265 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_blocking_lsm_notifier
- Explanation: register_blocking_lsm_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001266 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_page_bootmem_memmap
- Explanation: register_page_bootmem_memmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001267 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_vmap_purge_notifier
- Explanation: register_vmap_purge_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001268 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: release_child_resources
- Explanation: release_child_resources changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001269 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: release_pages
- Explanation: release_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001270 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: release_resource
- Explanation: release_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001272 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: remap_pfn_range_notrack
- Explanation: remap_pfn_range_notrack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001274 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: remap_vmalloc_range_partial
- Explanation: remap_vmalloc_range_partial changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001275 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: remcsum_offload
- Explanation: remcsum_offload changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001277 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: remove_resource
- Explanation: remove_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001278 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: remove_vm_area
- Explanation: remove_vm_area changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001279 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: replace_fd
- Explanation: replace_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001280 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: replace_mm_exe_file
- Explanation: replace_mm_exe_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001281 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_free_mem_region
- Explanation: request_free_mem_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001282 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_pending
- Explanation: request_pending changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001284 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: request_resource_conflict
- Explanation: request_resource_conflict changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001285 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reserve_bootmem_region
- Explanation: reserve_bootmem_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001286 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: reserve_region_with_split
- Explanation: reserve_region_with_split changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001287 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: resource_alignment
- Explanation: resource_alignment changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001288 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: resource_is_exclusive
- Explanation: resource_is_exclusive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001289 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: retain_state_shutdown
- Explanation: retain_state_shutdown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001290 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: retain_state_suspended
- Explanation: retain_state_suspended changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001291 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: root_device_unregister
- Explanation: root_device_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001292 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: runtime_auto
- Explanation: runtime_auto changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001293 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_mm_cid_after_execve
- Explanation: sched_mm_cid_after_execve changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001294 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_mm_cid_before_execve
- Explanation: sched_mm_cid_before_execve changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001295 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_mm_cid_exit_signals
- Explanation: sched_mm_cid_exit_signals changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001296 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_mm_cid_fork
- Explanation: sched_mm_cid_fork changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001298 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: scm_detach_fds_compat
- Explanation: scm_detach_fds_compat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001299 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: scm_fp_dup
- Explanation: scm_fp_dup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001301 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_audit_rule_free
- Explanation: security_audit_rule_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001302 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_audit_rule_init
- Explanation: security_audit_rule_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001303 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_audit_rule_known
- Explanation: security_audit_rule_known changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001304 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_audit_rule_match
- Explanation: security_audit_rule_match changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001305 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_binder_set_context_mgr
- Explanation: security_binder_set_context_mgr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001306 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_binder_transaction
- Explanation: security_binder_transaction changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001307 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_binder_transfer_binder
- Explanation: security_binder_transfer_binder changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001308 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_binder_transfer_file
- Explanation: security_binder_transfer_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001309 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_bprm_check
- Explanation: security_bprm_check changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001310 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_bprm_committed_creds
- Explanation: security_bprm_committed_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001311 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_bprm_committing_creds
- Explanation: security_bprm_committing_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001312 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_bprm_creds_for_exec
- Explanation: security_bprm_creds_for_exec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001313 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_bprm_creds_from_file
- Explanation: security_bprm_creds_from_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001314 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_capable
- Explanation: security_capable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001315 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_capget
- Explanation: security_capget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001316 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_capset
- Explanation: security_capset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001317 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_create_user_ns
- Explanation: security_create_user_ns changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001318 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_cred_alloc_blank
- Explanation: security_cred_alloc_blank changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001319 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_cred_free
- Explanation: security_cred_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001320 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_cred_getsecid
- Explanation: security_cred_getsecid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001321 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_current_getsecid_subj
- Explanation: security_current_getsecid_subj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001322 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_d_instantiate
- Explanation: security_d_instantiate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001323 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_dentry_create_files_as
- Explanation: security_dentry_create_files_as changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001324 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_dentry_init_security
- Explanation: security_dentry_init_security changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001325 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_alloc
- Explanation: security_file_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001326 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_fcntl
- Explanation: security_file_fcntl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001327 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_free
- Explanation: security_file_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001329 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_ioctl_compat
- Explanation: security_file_ioctl_compat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001330 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_lock
- Explanation: security_file_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001331 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_mprotect
- Explanation: security_file_mprotect changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001332 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_open
- Explanation: security_file_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001333 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_permission
- Explanation: security_file_permission changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001334 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_receive
- Explanation: security_file_receive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001335 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_send_sigiotask
- Explanation: security_file_send_sigiotask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001336 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_set_fowner
- Explanation: security_file_set_fowner changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001337 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_file_truncate
- Explanation: security_file_truncate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001338 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_free_mnt_opts
- Explanation: security_free_mnt_opts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001339 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_fs_context_dup
- Explanation: security_fs_context_dup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001340 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_fs_context_parse_param
- Explanation: security_fs_context_parse_param changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001341 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_fs_context_submount
- Explanation: security_fs_context_submount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001342 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_getprocattr
- Explanation: security_getprocattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001343 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_getselfattr
- Explanation: security_getselfattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001344 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inet_conn_established
- Explanation: security_inet_conn_established changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001345 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inet_conn_request
- Explanation: security_inet_conn_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001346 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inet_csk_clone
- Explanation: security_inet_csk_clone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001347 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_init
- Explanation: security_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001348 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_alloc
- Explanation: security_inode_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001350 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_copy_up_xattr
- Explanation: security_inode_copy_up_xattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001351 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_create
- Explanation: security_inode_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001352 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_follow_link
- Explanation: security_inode_follow_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001353 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_free
- Explanation: security_inode_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001354 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_get_acl
- Explanation: security_inode_get_acl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001355 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_getattr
- Explanation: security_inode_getattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001356 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_getsecctx
- Explanation: security_inode_getsecctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001357 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_getsecid
- Explanation: security_inode_getsecid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001358 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_getsecurity
- Explanation: security_inode_getsecurity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001359 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_getxattr
- Explanation: security_inode_getxattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001361 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_init_security_anon
- Explanation: security_inode_init_security_anon changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001362 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_invalidate_secctx
- Explanation: security_inode_invalidate_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001363 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_killpriv
- Explanation: security_inode_killpriv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001364 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_link
- Explanation: security_inode_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001365 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_listsecurity
- Explanation: security_inode_listsecurity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001366 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_listxattr
- Explanation: security_inode_listxattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001367 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_mkdir
- Explanation: security_inode_mkdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001368 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_mknod
- Explanation: security_inode_mknod changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001369 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_need_killpriv
- Explanation: security_inode_need_killpriv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001370 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_notifysecctx
- Explanation: security_inode_notifysecctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001371 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_permission
- Explanation: security_inode_permission changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001372 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_post_setxattr
- Explanation: security_inode_post_setxattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001373 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_readlink
- Explanation: security_inode_readlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001374 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_remove_acl
- Explanation: security_inode_remove_acl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001375 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_removexattr
- Explanation: security_inode_removexattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001376 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_rename
- Explanation: security_inode_rename changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001377 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_rmdir
- Explanation: security_inode_rmdir changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001378 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_set_acl
- Explanation: security_inode_set_acl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001379 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_setattr
- Explanation: security_inode_setattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001380 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_setsecctx
- Explanation: security_inode_setsecctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001381 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_setsecurity
- Explanation: security_inode_setsecurity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001382 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_setxattr
- Explanation: security_inode_setxattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001383 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_symlink
- Explanation: security_inode_symlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001384 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_inode_unlink
- Explanation: security_inode_unlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001385 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_ipc_getsecid
- Explanation: security_ipc_getsecid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001386 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_ipc_permission
- Explanation: security_ipc_permission changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001387 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_ismaclabel
- Explanation: security_ismaclabel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001388 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_kernel_act_as
- Explanation: security_kernel_act_as changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001389 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_kernel_create_files_as
- Explanation: security_kernel_create_files_as changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001390 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_kernel_load_data
- Explanation: security_kernel_load_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001391 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_kernel_module_request
- Explanation: security_kernel_module_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001392 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_kernel_post_load_data
- Explanation: security_kernel_post_load_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001393 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_kernel_post_read_file
- Explanation: security_kernel_post_read_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001394 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_kernel_read_file
- Explanation: security_kernel_read_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001395 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_kernfs_init_security
- Explanation: security_kernfs_init_security changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001396 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_key_alloc
- Explanation: security_key_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001397 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_key_free
- Explanation: security_key_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001398 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_key_getsecurity
- Explanation: security_key_getsecurity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001399 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_key_permission
- Explanation: security_key_permission changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001400 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_locked_down
- Explanation: security_locked_down changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001401 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_mmap_addr
- Explanation: security_mmap_addr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001402 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_mmap_file
- Explanation: security_mmap_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001403 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_move_mount
- Explanation: security_move_mount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001404 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_mptcp_add_subflow
- Explanation: security_mptcp_add_subflow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001405 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_msg_msg_alloc
- Explanation: security_msg_msg_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001406 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_msg_msg_free
- Explanation: security_msg_msg_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001407 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_msg_queue_alloc
- Explanation: security_msg_queue_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001408 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_msg_queue_associate
- Explanation: security_msg_queue_associate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001409 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_msg_queue_free
- Explanation: security_msg_queue_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001410 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_msg_queue_msgctl
- Explanation: security_msg_queue_msgctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001411 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_msg_queue_msgrcv
- Explanation: security_msg_queue_msgrcv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001412 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_msg_queue_msgsnd
- Explanation: security_msg_queue_msgsnd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001413 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_netlink_send
- Explanation: security_netlink_send changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001414 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_path_notify
- Explanation: security_path_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001415 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_perf_event_alloc
- Explanation: security_perf_event_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001416 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_perf_event_free
- Explanation: security_perf_event_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001417 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_perf_event_open
- Explanation: security_perf_event_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001418 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_perf_event_read
- Explanation: security_perf_event_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001419 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_perf_event_write
- Explanation: security_perf_event_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001420 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_prepare_creds
- Explanation: security_prepare_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001421 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_ptrace_access_check
- Explanation: security_ptrace_access_check changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001422 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_ptrace_traceme
- Explanation: security_ptrace_traceme changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001423 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_quota_on
- Explanation: security_quota_on changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001424 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_quotactl
- Explanation: security_quotactl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001425 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_release_secctx
- Explanation: security_release_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001426 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_req_classify_flow
- Explanation: security_req_classify_flow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001427 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_alloc
- Explanation: security_sb_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001428 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_clone_mnt_opts
- Explanation: security_sb_clone_mnt_opts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001429 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_delete
- Explanation: security_sb_delete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001430 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_eat_lsm_opts
- Explanation: security_sb_eat_lsm_opts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001431 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_free
- Explanation: security_sb_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001432 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_kern_mount
- Explanation: security_sb_kern_mount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001433 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_mnt_opts_compat
- Explanation: security_sb_mnt_opts_compat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001434 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_mount
- Explanation: security_sb_mount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001435 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_pivotroot
- Explanation: security_sb_pivotroot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001436 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_remount
- Explanation: security_sb_remount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001437 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_set_mnt_opts
- Explanation: security_sb_set_mnt_opts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001438 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_show_options
- Explanation: security_sb_show_options changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001439 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_statfs
- Explanation: security_sb_statfs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001440 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sb_umount
- Explanation: security_sb_umount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001441 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sctp_assoc_established
- Explanation: security_sctp_assoc_established changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001442 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sctp_assoc_request
- Explanation: security_sctp_assoc_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001443 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sctp_bind_connect
- Explanation: security_sctp_bind_connect changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001444 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sctp_sk_clone
- Explanation: security_sctp_sk_clone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001445 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_secctx_to_secid
- Explanation: security_secctx_to_secid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001446 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_secid_to_secctx
- Explanation: security_secid_to_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001447 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_secmark_refcount_dec
- Explanation: security_secmark_refcount_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001448 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_secmark_refcount_inc
- Explanation: security_secmark_refcount_inc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001449 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_secmark_relabel_packet
- Explanation: security_secmark_relabel_packet changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001450 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sem_alloc
- Explanation: security_sem_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001451 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sem_associate
- Explanation: security_sem_associate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001452 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sem_free
- Explanation: security_sem_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001453 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sem_semctl
- Explanation: security_sem_semctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001454 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sem_semop
- Explanation: security_sem_semop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001455 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_setprocattr
- Explanation: security_setprocattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001456 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_setselfattr
- Explanation: security_setselfattr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001457 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_settime64
- Explanation: security_settime64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001458 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_shm_alloc
- Explanation: security_shm_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001459 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_shm_associate
- Explanation: security_shm_associate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001460 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_shm_free
- Explanation: security_shm_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001461 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_shm_shmat
- Explanation: security_shm_shmat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001462 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_shm_shmctl
- Explanation: security_shm_shmctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001463 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sk_alloc
- Explanation: security_sk_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001464 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sk_classify_flow
- Explanation: security_sk_classify_flow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001465 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sk_clone
- Explanation: security_sk_clone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001466 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sk_free
- Explanation: security_sk_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001467 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sock_graft
- Explanation: security_sock_graft changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001468 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_sock_rcv_skb
- Explanation: security_sock_rcv_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001469 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_accept
- Explanation: security_socket_accept changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001470 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_bind
- Explanation: security_socket_bind changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001471 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_connect
- Explanation: security_socket_connect changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001472 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_create
- Explanation: security_socket_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001473 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_getpeername
- Explanation: security_socket_getpeername changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001474 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_getpeersec_dgram
- Explanation: security_socket_getpeersec_dgram changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001475 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_getpeersec_stream
- Explanation: security_socket_getpeersec_stream changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001476 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_getsockname
- Explanation: security_socket_getsockname changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001477 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_getsockopt
- Explanation: security_socket_getsockopt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001478 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_listen
- Explanation: security_socket_listen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001479 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_post_create
- Explanation: security_socket_post_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001480 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_recvmsg
- Explanation: security_socket_recvmsg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001481 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_sendmsg
- Explanation: security_socket_sendmsg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001482 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_setsockopt
- Explanation: security_socket_setsockopt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001483 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_shutdown
- Explanation: security_socket_shutdown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001484 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_socket_socketpair
- Explanation: security_socket_socketpair changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001485 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_syslog
- Explanation: security_syslog changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001486 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_alloc
- Explanation: security_task_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001487 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_fix_setgid
- Explanation: security_task_fix_setgid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001488 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_fix_setgroups
- Explanation: security_task_fix_setgroups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001489 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_fix_setuid
- Explanation: security_task_fix_setuid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001490 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_free
- Explanation: security_task_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001491 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_getioprio
- Explanation: security_task_getioprio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001492 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_getpgid
- Explanation: security_task_getpgid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001493 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_getscheduler
- Explanation: security_task_getscheduler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001494 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_getsecid_obj
- Explanation: security_task_getsecid_obj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001495 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_getsid
- Explanation: security_task_getsid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001496 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_kill
- Explanation: security_task_kill changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001497 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_movememory
- Explanation: security_task_movememory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001498 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_prctl
- Explanation: security_task_prctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001499 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_prlimit
- Explanation: security_task_prlimit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001500 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_setioprio
- Explanation: security_task_setioprio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001501 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_setnice
- Explanation: security_task_setnice changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001502 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_setpgid
- Explanation: security_task_setpgid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001503 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_setrlimit
- Explanation: security_task_setrlimit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001504 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_setscheduler
- Explanation: security_task_setscheduler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001505 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_task_to_inode
- Explanation: security_task_to_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001506 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_transfer_creds
- Explanation: security_transfer_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001507 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_tun_dev_alloc_security
- Explanation: security_tun_dev_alloc_security changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001509 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_tun_dev_attach_queue
- Explanation: security_tun_dev_attach_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001510 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_tun_dev_create
- Explanation: security_tun_dev_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001511 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_tun_dev_free_security
- Explanation: security_tun_dev_free_security changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001512 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_tun_dev_open
- Explanation: security_tun_dev_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001513 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_unix_may_send
- Explanation: security_unix_may_send changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001514 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_unix_stream_connect
- Explanation: security_unix_stream_connect changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001515 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_uring_cmd
- Explanation: security_uring_cmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001516 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_uring_override_creds
- Explanation: security_uring_override_creds changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001517 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_uring_sqpoll
- Explanation: security_uring_sqpoll changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001518 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: security_vm_enough_memory_mm
- Explanation: security_vm_enough_memory_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001522 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_close_on_exec
- Explanation: set_close_on_exec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001523 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_dma_reserve
- Explanation: set_dma_reserve changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001524 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_dumpable
- Explanation: set_dumpable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001525 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_mm_exe_file
- Explanation: set_mm_exe_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001527 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_page_dirty_lock
- Explanation: set_page_dirty_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001528 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_page_writeback
- Explanation: set_page_writeback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'page', 'type': '*mut page'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'page', 'type': '*mut page'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-001529 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_pgdat_percpu_threshold
- Explanation: set_pgdat_percpu_threshold changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001530 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_primary_fwnode
- Explanation: set_primary_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001531 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_pte_range
- Explanation: set_pte_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001532 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_sched_topology
- Explanation: set_sched_topology changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001533 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_secondary_fwnode
- Explanation: set_secondary_fwnode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001535 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setup_initial_init_mm
- Explanation: setup_initial_init_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001536 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setup_nr_node_ids
- Explanation: setup_nr_node_ids changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001537 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: setup_per_cpu_pageset
- Explanation: setup_per_cpu_pageset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001538 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_alloc_append_table_from_pages
- Explanation: sg_alloc_append_table_from_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001540 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_alloc_table_chained
- Explanation: sg_alloc_table_chained changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001541 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_alloc_table_from_pages_segment
- Explanation: sg_alloc_table_from_pages_segment changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001542 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_copy_buffer
- Explanation: sg_copy_buffer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001543 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_copy_from_buffer
- Explanation: sg_copy_from_buffer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001544 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_copy_to_buffer
- Explanation: sg_copy_to_buffer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001545 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_free_append_table
- Explanation: sg_free_append_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001547 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_free_table_chained
- Explanation: sg_free_table_chained changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001548 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_init_one
- Explanation: sg_init_one changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001549 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_init_table
- Explanation: sg_init_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001550 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_last
- Explanation: sg_last changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001551 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_miter_next
- Explanation: sg_miter_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001552 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_miter_skip
- Explanation: sg_miter_skip changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001553 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_miter_start
- Explanation: sg_miter_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001554 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_miter_stop
- Explanation: sg_miter_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001556 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_nents_for_len
- Explanation: sg_nents_for_len changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001557 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_next
- Explanation: sg_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001558 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_pcopy_from_buffer
- Explanation: sg_pcopy_from_buffer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001559 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_pcopy_to_buffer
- Explanation: sg_pcopy_to_buffer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001560 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_split
- Explanation: sg_split changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001561 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sg_zero_buffer
- Explanation: sg_zero_buffer changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001563 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sgl_alloc_order
- Explanation: sgl_alloc_order changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001565 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sgl_free_n_order
- Explanation: sgl_free_n_order changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001566 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sgl_free_order
- Explanation: sgl_free_order changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001567 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: shake_page
- Explanation: shake_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001569 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: show_class_attr_string
- Explanation: show_class_attr_string changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001571 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: si_mem_available
- Explanation: si_mem_available changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001573 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: si_meminfo_node
- Explanation: si_meminfo_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001574 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: single_hugepage_flag_show
- Explanation: single_hugepage_flag_show changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001575 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: single_hugepage_flag_store
- Explanation: single_hugepage_flag_store changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001576 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: siphash_1u32
- Explanation: siphash_1u32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001577 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: siphash_1u64
- Explanation: siphash_1u64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001578 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: siphash_2u64
- Explanation: siphash_2u64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001579 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: siphash_3u32
- Explanation: siphash_3u32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001580 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: siphash_3u64
- Explanation: siphash_3u64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001581 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: siphash_4u64
- Explanation: siphash_4u64 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001582 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_abort_seq_read
- Explanation: skb_abort_seq_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001583 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_add_rx_frag
- Explanation: skb_add_rx_frag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001585 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_append_pagefrags
- Explanation: skb_append_pagefrags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001586 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_attempt_defer_free
- Explanation: skb_attempt_defer_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001588 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_checksum_setup
- Explanation: skb_checksum_setup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001589 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_checksum_trimmed
- Explanation: skb_checksum_trimmed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001591 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_clone_sk
- Explanation: skb_clone_sk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001592 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_coalesce_rx_frag
- Explanation: skb_coalesce_rx_frag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001593 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_complete_tx_timestamp
- Explanation: skb_complete_tx_timestamp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001594 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_complete_wifi_ack
- Explanation: skb_complete_wifi_ack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001595 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_condense
- Explanation: skb_condense changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001597 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_and_csum_bits
- Explanation: skb_copy_and_csum_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001598 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_and_csum_datagram_msg
- Explanation: skb_copy_and_csum_datagram_msg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001599 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_and_csum_dev
- Explanation: skb_copy_and_csum_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001600 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_and_hash_datagram_iter
- Explanation: skb_copy_and_hash_datagram_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001601 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_bits
- Explanation: skb_copy_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001602 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_datagram_from_iter
- Explanation: skb_copy_datagram_from_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001603 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_datagram_iter
- Explanation: skb_copy_datagram_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001604 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_expand
- Explanation: skb_copy_expand changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001605 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_header
- Explanation: skb_copy_header changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001606 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_ubufs
- Explanation: skb_copy_ubufs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001607 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_cow_data
- Explanation: skb_cow_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001609 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_dequeue_tail
- Explanation: skb_dequeue_tail changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001610 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_dump
- Explanation: skb_dump changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001612 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_ensure_writable_head_tail
- Explanation: skb_ensure_writable_head_tail changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001613 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_errqueue_purge
- Explanation: skb_errqueue_purge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001614 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_eth_pop
- Explanation: skb_eth_pop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001615 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_eth_push
- Explanation: skb_eth_push changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001616 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_expand_head
- Explanation: skb_expand_head changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001617 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_ext_add
- Explanation: skb_ext_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001618 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_find_text
- Explanation: skb_find_text changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001619 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_flow_dissect_ct
- Explanation: skb_flow_dissect_ct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001620 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_flow_dissect_hash
- Explanation: skb_flow_dissect_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001621 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_flow_dissect_meta
- Explanation: skb_flow_dissect_meta changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001622 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_flow_dissect_tunnel_info
- Explanation: skb_flow_dissect_tunnel_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001623 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_flow_dissector_init
- Explanation: skb_flow_dissector_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001624 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_flow_get_icmp_tci
- Explanation: skb_flow_get_icmp_tci changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001625 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_free_datagram
- Explanation: skb_free_datagram changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001626 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_get_hash_perturb
- Explanation: skb_get_hash_perturb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001627 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_get_poff
- Explanation: skb_get_poff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001628 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_headers_offset_update
- Explanation: skb_headers_offset_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001629 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_init
- Explanation: skb_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001630 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_kill_datagram
- Explanation: skb_kill_datagram changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001631 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_morph
- Explanation: skb_morph changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001632 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_mpls_dec_ttl
- Explanation: skb_mpls_dec_ttl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001633 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_mpls_pop
- Explanation: skb_mpls_pop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001634 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_mpls_push
- Explanation: skb_mpls_push changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001635 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_mpls_update_lse
- Explanation: skb_mpls_update_lse changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001636 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_page_frag_refill
- Explanation: skb_page_frag_refill changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001637 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_partial_csum_set
- Explanation: skb_partial_csum_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001638 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_prepare_seq_read
- Explanation: skb_prepare_seq_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001640 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_pull_data
- Explanation: skb_pull_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001641 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_pull_rcsum
- Explanation: skb_pull_rcsum changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001642 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_push
- Explanation: skb_push changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001643 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_put
- Explanation: skb_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001644 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_queue_head
- Explanation: skb_queue_head changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001645 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_queue_purge_reason
- Explanation: skb_queue_purge_reason changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001646 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_queue_tail
- Explanation: skb_queue_tail changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001647 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_rbtree_purge
- Explanation: skb_rbtree_purge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001648 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_realloc_headroom
- Explanation: skb_realloc_headroom changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001649 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_recv_datagram
- Explanation: skb_recv_datagram changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001650 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_release_head_state
- Explanation: skb_release_head_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001651 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_scrub_packet
- Explanation: skb_scrub_packet changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001653 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_segment_list
- Explanation: skb_segment_list changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001655 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_send_sock_locked
- Explanation: skb_send_sock_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001656 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_seq_read
- Explanation: skb_seq_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001657 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_shift
- Explanation: skb_shift changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001658 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_splice_bits
- Explanation: skb_splice_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001659 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_splice_from_iter
- Explanation: skb_splice_from_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001660 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_split
- Explanation: skb_split changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001661 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_store_bits
- Explanation: skb_store_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001663 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_to_sgvec_nomark
- Explanation: skb_to_sgvec_nomark changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001664 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_trim
- Explanation: skb_trim changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001665 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_try_coalesce
- Explanation: skb_try_coalesce changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001666 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_tstamp_tx
- Explanation: skb_tstamp_tx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001667 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_tx_error
- Explanation: skb_tx_error changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001668 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_unlink
- Explanation: skb_unlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001669 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_vlan_pop
- Explanation: skb_vlan_pop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001670 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_vlan_push
- Explanation: skb_vlan_push changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001671 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_vlan_untag
- Explanation: skb_vlan_untag changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001673 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_zerocopy_headlen
- Explanation: skb_zerocopy_headlen changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001674 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_zerocopy_iter_stream
- Explanation: skb_zerocopy_iter_stream changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001675 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: slab_build_skb
- Explanation: slab_build_skb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001676 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: slot
- Explanation: slot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001677 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: slow_gro
- Explanation: slow_gro changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001679 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sock_alloc_file
- Explanation: sock_alloc_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001681 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sock_create_kern
- Explanation: sock_create_kern changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001682 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sock_create_lite
- Explanation: sock_create_lite changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001683 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sock_from_file
- Explanation: sock_from_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001684 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sock_is_registered
- Explanation: sock_is_registered changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001685 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sock_recvmsg
- Explanation: sock_recvmsg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001686 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sock_register
- Explanation: sock_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001687 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sock_release
- Explanation: sock_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001688 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sock_sendmsg
- Explanation: sock_sendmsg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001689 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sock_unregister
- Explanation: sock_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001690 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sock_wake_async
- Explanation: sock_wake_async changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001691 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sockfd_lookup
- Explanation: sockfd_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001692 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: soft_offline_page
- Explanation: soft_offline_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001693 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sparse_buffer_alloc
- Explanation: sparse_buffer_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001694 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: split_page
- Explanation: split_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001696 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_early_init
- Explanation: stack_depot_early_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001697 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_fetch
- Explanation: stack_depot_fetch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001698 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_get_extra_bits
- Explanation: stack_depot_get_extra_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001699 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_init
- Explanation: stack_depot_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001700 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_print
- Explanation: stack_depot_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001701 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_put
- Explanation: stack_depot_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001702 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_request_early_init
- Explanation: stack_depot_request_early_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001704 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_save_flags
- Explanation: stack_depot_save_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001705 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_set_extra_bits
- Explanation: stack_depot_set_extra_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001706 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_snprint
- Explanation: stack_depot_snprint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001707 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_trace_print
- Explanation: stack_trace_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001709 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_trace_save_regs
- Explanation: stack_trace_save_regs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001711 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_trace_save_tsk_reliable
- Explanation: stack_trace_save_tsk_reliable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001712 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_trace_save_user
- Explanation: stack_trace_save_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001713 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_trace_snprint
- Explanation: stack_trace_snprint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001714 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: state_synced
- Explanation: state_synced changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001716 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: subsys_interface_register
- Explanation: subsys_interface_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001717 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: subsys_interface_unregister
- Explanation: subsys_interface_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001718 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: subsys_system_register
- Explanation: subsys_system_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001719 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: subsys_virtual_register
- Explanation: subsys_virtual_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001720 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sum_zone_node_page_state
- Explanation: sum_zone_node_page_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001721 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sum_zone_numa_event_state
- Explanation: sum_zone_numa_event_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001722 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: supports_gmii
- Explanation: supports_gmii changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001724 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: suspended_by_mdio_bus
- Explanation: suspended_by_mdio_bus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001725 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sw_hash
- Explanation: sw_hash changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001726 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: switch_task_namespaces
- Explanation: switch_task_namespaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001727 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: synchronize_hardirq
- Explanation: synchronize_hardirq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001728 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: synchronize_irq
- Explanation: synchronize_irq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001731 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: syscore
- Explanation: syscore changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001732 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysctl_vm_numa_stat_handler
- Explanation: sysctl_vm_numa_stat_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001733 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_format_mac
- Explanation: sysfs_format_mac changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001734 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sysfs_links
- Explanation: sysfs_links changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001736 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: tc_skip_classify
- Explanation: tc_skip_classify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001737 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: timer_autosuspends
- Explanation: timer_autosuspends changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001739 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: track_pfn_copy
- Explanation: track_pfn_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001740 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: track_pfn_insert
- Explanation: track_pfn_insert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001741 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: track_pfn_remap
- Explanation: track_pfn_remap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001744 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: truncate_inode_pages_final
- Explanation: truncate_inode_pages_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001745 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: truncate_inode_pages_range
- Explanation: truncate_inode_pages_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001747 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: truncate_pagecache_range
- Explanation: truncate_pagecache_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001748 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: truncate_setsize
- Explanation: truncate_setsize changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001750 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unlink_file_vma
- Explanation: unlink_file_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001751 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unlock_device_hotplug
- Explanation: unlock_device_hotplug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001752 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unmap_mapping_pages
- Explanation: unmap_mapping_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001753 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unmap_mapping_range
- Explanation: unmap_mapping_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001754 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unmap_vmas
- Explanation: unmap_vmas changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001756 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unpin_user_page_range_dirty_lock
- Explanation: unpin_user_page_range_dirty_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001758 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unpin_user_pages_dirty_lock
- Explanation: unpin_user_pages_dirty_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001759 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unpoison_memory
- Explanation: unpoison_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001760 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_blocking_lsm_notifier
- Explanation: unregister_blocking_lsm_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001761 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unregister_vmap_purge_notifier
- Explanation: unregister_vmap_purge_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001762 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unshare_nsproxy_namespaces
- Explanation: unshare_nsproxy_namespaces changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001764 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: untrack_pfn_clear
- Explanation: untrack_pfn_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001765 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: unxlate_dev_mem_ptr
- Explanation: unxlate_dev_mem_ptr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001766 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: use_autosuspend
- Explanation: use_autosuspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001767 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: use_mwaitx_delay
- Explanation: use_mwaitx_delay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001768 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: use_tpause_delay
- Explanation: use_tpause_delay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001769 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: use_tsc_delay
- Explanation: use_tsc_delay changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001770 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: user_shm_lock
- Explanation: user_shm_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001771 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: user_shm_unlock
- Explanation: user_shm_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001772 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: usleep_range_state
- Explanation: usleep_range_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001773 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: valid_mmap_phys_addr_range
- Explanation: valid_mmap_phys_addr_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001774 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: valid_phys_addr_range
- Explanation: valid_phys_addr_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001775 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vcalloc
- Explanation: vcalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001779 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vfree_atomic
- Explanation: vfree_atomic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001780 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vlan_dei
- Explanation: vlan_dei changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001781 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vlan_id
- Explanation: vlan_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001782 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vlan_priority
- Explanation: vlan_priority changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001783 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_area_add_early
- Explanation: vm_area_add_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001784 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_area_alloc
- Explanation: vm_area_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001785 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_area_dup
- Explanation: vm_area_dup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001786 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_area_free
- Explanation: vm_area_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001787 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_area_register_early
- Explanation: vm_area_register_early changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001788 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_brk_flags
- Explanation: vm_brk_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001789 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_events_fold_cpu
- Explanation: vm_events_fold_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001790 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_get_page_prot
- Explanation: vm_get_page_prot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001792 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_insert_pages
- Explanation: vm_insert_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001793 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_iomap_memory
- Explanation: vm_iomap_memory changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001795 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_map_pages_zero
- Explanation: vm_map_pages_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001796 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_map_ram
- Explanation: vm_map_ram changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001798 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_munmap
- Explanation: vm_munmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001800 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_normal_folio_pmd
- Explanation: vm_normal_folio_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001802 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_normal_page_pmd
- Explanation: vm_normal_page_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001803 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_stat_account
- Explanation: vm_stat_account changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001804 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_unmap_aliases
- Explanation: vm_unmap_aliases changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001805 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vm_unmap_ram
- Explanation: vm_unmap_ram changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001807 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_expand
- Explanation: vma_expand changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001809 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_interval_tree_insert_after
- Explanation: vma_interval_tree_insert_after changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001810 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_interval_tree_iter_first
- Explanation: vma_interval_tree_iter_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001811 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_interval_tree_iter_next
- Explanation: vma_interval_tree_iter_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001812 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_interval_tree_remove
- Explanation: vma_interval_tree_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001813 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_is_anon_shmem
- Explanation: vma_is_anon_shmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001814 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_is_shmem
- Explanation: vma_is_shmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001815 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_is_special_mapping
- Explanation: vma_is_special_mapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001816 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_is_stack_for_current
- Explanation: vma_is_stack_for_current changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001817 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_modify
- Explanation: vma_modify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001818 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_needs_dirty_tracking
- Explanation: vma_needs_dirty_tracking changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001819 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_set_file
- Explanation: vma_set_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001820 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_set_page_prot
- Explanation: vma_set_page_prot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001821 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_shrink
- Explanation: vma_shrink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001822 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vma_wants_writenotify
- Explanation: vma_wants_writenotify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001825 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmalloc_32_user
- Explanation: vmalloc_32_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001826 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmalloc_array
- Explanation: vmalloc_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001827 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmalloc_dump_obj
- Explanation: vmalloc_dump_obj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001828 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmalloc_huge
- Explanation: vmalloc_huge changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001829 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmalloc_node
- Explanation: vmalloc_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001830 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmalloc_nr_pages
- Explanation: vmalloc_nr_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001831 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmalloc_to_page
- Explanation: vmalloc_to_page changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001832 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmalloc_to_pfn
- Explanation: vmalloc_to_pfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001833 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmalloc_user
- Explanation: vmalloc_user changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001835 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmap_pfn
- Explanation: vmap_pfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001837 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_alloc_block_buf
- Explanation: vmemmap_alloc_block_buf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001838 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_check_pmd
- Explanation: vmemmap_check_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001839 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_p4d_populate
- Explanation: vmemmap_p4d_populate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001840 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_pgd_populate
- Explanation: vmemmap_pgd_populate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001841 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_pmd_populate
- Explanation: vmemmap_pmd_populate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001843 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_populate_basepages
- Explanation: vmemmap_populate_basepages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001844 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_populate_hugepages
- Explanation: vmemmap_populate_hugepages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001845 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_populate_print_last
- Explanation: vmemmap_populate_print_last changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001846 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_pte_populate
- Explanation: vmemmap_pte_populate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001847 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_pud_populate
- Explanation: vmemmap_pud_populate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001848 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_set_pmd
- Explanation: vmemmap_set_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001849 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmemmap_verify
- Explanation: vmemmap_verify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001851 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmf_insert_mixed_mkwrite
- Explanation: vmf_insert_mixed_mkwrite changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001853 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmf_insert_pfn_pmd
- Explanation: vmf_insert_pfn_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001854 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmf_insert_pfn_prot
- Explanation: vmf_insert_pfn_prot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001855 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmf_insert_pfn_pud
- Explanation: vmf_insert_pfn_pud changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001856 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vmstat_refresh
- Explanation: vmstat_refresh changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001857 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vread_iter
- Explanation: vread_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001859 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vunmap_range
- Explanation: vunmap_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001861 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: vzalloc_node
- Explanation: vzalloc_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001862 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wait_for_device_probe
- Explanation: wait_for_device_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001863 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wait_for_init_devices_probe
- Explanation: wait_for_init_devices_probe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001864 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wake_up_if_idle
- Explanation: wake_up_if_idle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001865 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_path
- Explanation: wakeup_path changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001866 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_source_add
- Explanation: wakeup_source_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001867 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_source_create
- Explanation: wakeup_source_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001868 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_source_destroy
- Explanation: wakeup_source_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001869 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_source_register
- Explanation: wakeup_source_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001870 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_source_remove
- Explanation: wakeup_source_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001871 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_source_unregister
- Explanation: wakeup_source_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001872 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_sources_read_lock
- Explanation: wakeup_sources_read_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001873 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_sources_read_unlock
- Explanation: wakeup_sources_read_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001874 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_sources_walk_next
- Explanation: wakeup_sources_walk_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001875 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wakeup_sources_walk_start
- Explanation: wakeup_sources_walk_start changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001876 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: walk_iomem_res_desc
- Explanation: walk_iomem_res_desc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001877 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: walk_mem_res
- Explanation: walk_mem_res changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001878 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: walk_system_ram_range
- Explanation: walk_system_ram_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001880 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: walk_system_ram_res_rev
- Explanation: walk_system_ram_res_rev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001881 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: warn_alloc
- Explanation: warn_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001883 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wifi_acked_valid
- Explanation: wifi_acked_valid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001884 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wol_enabled
- Explanation: wol_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001886 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: workqueue_unbound_exclude_cpumask
- Explanation: workqueue_unbound_exclude_cpumask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001887 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: xlate_dev_mem_ptr
- Explanation: xlate_dev_mem_ptr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001888 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: zap_huge_pmd
- Explanation: zap_huge_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001889 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: zap_huge_pud
- Explanation: zap_huge_pud changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001890 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: zap_page_range_single
- Explanation: zap_page_range_single changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001891 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: zap_vma_ptes
- Explanation: zap_vma_ptes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001893 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: zerocopy_sg_from_iter
- Explanation: zerocopy_sg_from_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001942 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bool
- Explanation: bool changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['*drm_vblank_get_scanout_position_func)(struct drm_crtc *crtc, bool in_vblank_irq, int *vpos, int *hpos, ktime_t *stime, ktime_t *etime, const struct drm_display_mode *mode'], 'return_type': 'typedef'}`
- New: `{'params': ['*dl_server_has_tasks_f)(struct sched_dl_entity *'], 'return_type': 'typedef'}`

### Rust Evidence

- Graph edges: `1`

## W-001927 FieldDrift

- Risk: High
- Score: 10.4
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'saved_state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': '__bindgen_padding_1', 'type': '[u64; 4usize]'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_2', 'type': '[u64; 2usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'core::ffi::c_uint'}, {'name': 'saved_state', 'type': 'core::ffi::c_uint'}, {'name': 'stack', 'type': '*mut core::ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'ptrace', 'type': 'core::ffi::c_uint'}, {'name': 'on_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'core::ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'core::ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'core::ffi::c_int'}, {'name': 'wake_cpu', 'type': 'core::ffi::c_int'}, {'name': 'on_rq', 'type': 'core::ffi::c_int'}, {'name': 'prio', 'type': 'core::ffi::c_int'}, {'name': 'static_prio', 'type': 'core::ffi::c_int'}, {'name': 'normal_prio', 'type': 'core::ffi::c_int'}, {'name': 'rt_priority', 'type': 'core::ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'core::ffi::c_uint'}, {'name': 'policy', 'type': 'core::ffi::c_uint'}, {'name': 'nr_cpus_allowed', 'type': 'core::ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut core::ffi::c_void'}, {'name': 'migration_disabled', 'type': 'core::ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'core::ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'core::ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'core::ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'core::ffi::c_int'}, {'name': 'exit_code', 'type': 'core::ffi::c_int'}, {'name': 'exit_signal', 'type': 'core::ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'core::ffi::c_int'}, {'name': 'jobctl', 'type': 'core::ffi::c_ulong'}, {'name': 'personality', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'core::ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'core::ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut core::ffi::c_int'}, {'name': 'worker_private', 'type': '*mut core::ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'core::ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'core::ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'core::ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'core::ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'core::ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut core::ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'core::ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cpuset_slab_spread_rotor', 'type': 'core::ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'core::ffi::c_uint'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'core::ffi::c_short'}, {'name': 'pref_node_fork', 'type': 'core::ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'core::ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'core::ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'core::ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'core::ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'core::ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'core::ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'core::ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'core::ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'core::ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_vaddr', 'type': '*mut core::ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'core::ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 2usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `9`

## W-001901 FieldDrift

- Risk: High
- Score: 10.2
- Symbol: dentry
- Explanation: dentry changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'd_flags', 'type': 'core::ffi::c_uint'}, {'name': 'd_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'd_hash', 'type': 'hlist_bl_node'}, {'name': 'd_parent', 'type': '*mut dentry'}, {'name': 'd_name', 'type': 'qstr'}, {'name': 'd_inode', 'type': '*mut inode'}, {'name': 'd_iname', 'type': '[core::ffi::c_uchar; 32usize]'}, {'name': 'd_lockref', 'type': 'lockref'}, {'name': 'd_op', 'type': '*const dentry_operations'}, {'name': 'd_sb', 'type': '*mut super_block'}, {'name': 'd_time', 'type': 'core::ffi::c_ulong'}, {'name': 'd_fsdata', 'type': '*mut core::ffi::c_void'}, {'name': '__bindgen_anon_1', 'type': 'dentry__bindgen_ty_1'}, {'name': 'd_child', 'type': 'list_head'}, {'name': 'd_subdirs', 'type': 'list_head'}, {'name': 'd_u', 'type': 'dentry__bindgen_ty_2'}]`
- New: `[{'name': 'd_flags', 'type': 'core::ffi::c_uint'}, {'name': 'd_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'd_hash', 'type': 'hlist_bl_node'}, {'name': 'd_parent', 'type': '*mut dentry'}, {'name': 'd_name', 'type': 'qstr'}, {'name': 'd_inode', 'type': '*mut inode'}, {'name': 'd_iname', 'type': '[core::ffi::c_uchar; 40usize]'}, {'name': 'd_lockref', 'type': 'lockref'}, {'name': 'd_op', 'type': '*const dentry_operations'}, {'name': 'd_sb', 'type': '*mut super_block'}, {'name': 'd_time', 'type': 'core::ffi::c_ulong'}, {'name': 'd_fsdata', 'type': '*mut core::ffi::c_void'}, {'name': '__bindgen_anon_1', 'type': 'dentry__bindgen_ty_1'}, {'name': 'd_sib', 'type': 'hlist_node'}, {'name': 'd_children', 'type': 'hlist_head'}, {'name': 'd_u', 'type': 'dentry__bindgen_ty_2'}]`

### Rust Evidence

- Graph edges: `8`

## W-001925 FieldDrift

- Risk: High
- Score: 10.2
- Symbol: socket
- Explanation: socket changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'state', 'type': 'socket_state'}, {'name': 'type_', 'type': 'core::ffi::c_short'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'file', 'type': '*mut file'}, {'name': 'sk', 'type': '*mut sock'}, {'name': 'ops', 'type': '*const proto_ops'}, {'name': '__bindgen_padding_0', 'type': '[u64; 3usize]'}, {'name': 'wq', 'type': 'socket_wq'}]`

### Rust Evidence

- Graph edges: `8`

## W-001896 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: anon_vma
- Explanation: anon_vma changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `7`

## W-000013 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __d_lookup_rcu
- Explanation: __d_lookup_rcu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000038 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __get_task_ioprio
- Explanation: __get_task_ioprio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000100 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __reserved_1
- Explanation: __reserved_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000101 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __reserved_2
- Explanation: __reserved_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000102 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __reserved_3
- Explanation: __reserved_3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000104 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __rseq_handle_notify_resume
- Explanation: __rseq_handle_notify_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000107 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __secure_computing
- Explanation: __secure_computing changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000159 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: _paravirt_nop
- Explanation: _paravirt_nop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000182 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: apic_enabled
- Explanation: apic_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000204 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: backing_file_open
- Explanation: backing_file_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000256 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: check_fsmapping
- Explanation: check_fsmapping changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000305 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: d_genocide
- Explanation: d_genocide changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000306 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: d_instantiate_anon
- Explanation: d_instantiate_anon changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000307 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: d_instantiate_unique
- Explanation: d_instantiate_unique changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000308 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: d_set_fallthru
- Explanation: d_set_fallthru changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000315 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: delivery_mode
- Explanation: delivery_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000316 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: delivery_status
- Explanation: delivery_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000317 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: destination_mode
- Explanation: destination_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000444 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: divisor
- Explanation: divisor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000482 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: do_clone_file_range
- Explanation: do_clone_file_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000489 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: do_splice_direct
- Explanation: do_splice_direct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000588 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: focus_cpu
- Explanation: focus_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000618 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: generic_copy_file_range
- Explanation: generic_copy_file_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000673 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: get_active_super
- Explanation: get_active_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000683 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: get_seccomp_filter
- Explanation: get_seccomp_filter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000707 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: illegal_register_address
- Explanation: illegal_register_address changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000708 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: import_single_range
- Explanation: import_single_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000855 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: level
- Explanation: level changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000873 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: logical_dest
- Explanation: logical_dest changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000881 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mas_is_err
- Explanation: mas_is_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000883 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: max_lvt
- Explanation: max_lvt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000958 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: model
- Explanation: model changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001050 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: paravirt_BUG
- Explanation: paravirt_BUG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001184 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phys_apic_id
- Explanation: phys_apic_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001185 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: phys_dest
- Explanation: phys_dest changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001193 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: plist_add
- Explanation: plist_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001194 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: plist_del
- Explanation: plist_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001195 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: plist_requeue
- Explanation: plist_requeue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001229 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: polarity
- Explanation: polarity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001231 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: prctl_get_seccomp
- Explanation: prctl_get_seccomp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001232 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: prctl_set_seccomp
- Explanation: prctl_set_seccomp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001234 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: priority
- Explanation: priority changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001256 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: recalc_sigpending_and_wake
- Explanation: recalc_sigpending_and_wake changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001257 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: receive_accept_error
- Explanation: receive_accept_error changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001258 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: receive_cs_error
- Explanation: receive_cs_error changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001261 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: receive_illegal_vector
- Explanation: receive_illegal_vector changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001276 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: remote_irr
- Explanation: remote_irr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001300 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: seccomp_filter_release
- Explanation: seccomp_filter_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001519 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: send_accept_error
- Explanation: send_accept_error changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001520 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: send_cs_error
- Explanation: send_cs_error changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001521 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: send_illegal_vector
- Explanation: send_illegal_vector changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001534 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: set_syscall_user_dispatch
- Explanation: set_syscall_user_dispatch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001568 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: shorthand
- Explanation: shorthand changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001570 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: shrink_dcache_for_umount
- Explanation: shrink_dcache_for_umount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001695 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: spurious_vector
- Explanation: spurious_vector changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001715 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: strlcpy
- Explanation: strlcpy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001729 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: syscall_user_dispatch_get_config
- Explanation: syscall_user_dispatch_get_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001730 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: syscall_user_dispatch_set_config
- Explanation: syscall_user_dispatch_set_config changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001738 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: timer_mode
- Explanation: timer_mode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001742 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: trigger
- Explanation: trigger changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001776 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vector
- Explanation: vector changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001777 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: version
- Explanation: version changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001885 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: workqueue_set_unbound_cpumask
- Explanation: workqueue_set_unbound_cpumask changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-001902 FieldDrift

- Risk: Medium
- Score: 9.6
- Symbol: dev_pagemap
- Explanation: dev_pagemap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'altmap', 'type': 'vmem_altmap'}, {'name': 'ref_', 'type': 'percpu_ref'}, {'name': 'done', 'type': 'completion'}, {'name': 'type_', 'type': 'memory_type'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': 'vmemmap_shift', 'type': 'core::ffi::c_ulong'}, {'name': 'ops', 'type': '*const dev_pagemap_ops'}, {'name': 'owner', 'type': '*mut core::ffi::c_void'}, {'name': 'nr_range', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_anon_1', 'type': 'dev_pagemap__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `5`

## W-001928 FieldDrift

- Risk: Medium
- Score: 9.6
- Symbol: ubuf_info
- Explanation: ubuf_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'callback', 'type': '::core::option::Option<'}, {'name': 'refcnt', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'u8_'}]`

### Rust Evidence

- Graph edges: `5`

## W-001943 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: dev_get_drvdata
- Explanation: dev_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['&dsi->dev'], 'return_type': 'return'}`
- New: `{'params': ['&mdio->dev'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001906 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: kunit_suite
- Explanation: kunit_suite changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '[core::ffi::c_char; 256usize]'}, {'name': 'suite_exit', 'type': '::core::option::Option<unsafe extern "C" fn(suite: *mut kunit_suite)>'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit) -> core::ffi::c_int>'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'test_cases', 'type': '*mut kunit_case'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status_comment', 'type': '[core::ffi::c_char; 256usize]'}, {'name': 'debugfs', 'type': '*mut dentry'}, {'name': 'log', 'type': '*mut string_stream'}, {'name': 'suite_init_err', 'type': 'core::ffi::c_int'}]`
- New: `[{'name': 'name', 'type': '[core::ffi::c_char; 256usize]'}, {'name': 'suite_exit', 'type': '::core::option::Option<unsafe extern "C" fn(suite: *mut kunit_suite)>'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit) -> core::ffi::c_int>'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'test_cases', 'type': '*mut kunit_case'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status_comment', 'type': '[core::ffi::c_char; 256usize]'}, {'name': 'debugfs', 'type': '*mut dentry'}, {'name': 'log', 'type': '*mut string_stream'}, {'name': 'suite_init_err', 'type': 'core::ffi::c_int'}, {'name': 'is_init', 'type': 'bool_'}]`

### Rust Evidence

- Graph edges: `4`

## W-001907 FieldDrift

- Risk: Medium
- Score: 9.4
- Symbol: lruvec
- Explanation: lruvec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lists', 'type': '[list_head; 5usize]'}, {'name': 'lru_lock', 'type': 'spinlock_t'}, {'name': 'anon_cost', 'type': 'core::ffi::c_ulong'}, {'name': 'file_cost', 'type': 'core::ffi::c_ulong'}, {'name': 'nonresident_age', 'type': 'atomic_long_t'}, {'name': 'refaults', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}]`
- New: `[{'name': 'lists', 'type': '[list_head; 5usize]'}, {'name': 'lru_lock', 'type': 'spinlock_t'}, {'name': 'anon_cost', 'type': 'core::ffi::c_ulong'}, {'name': 'file_cost', 'type': 'core::ffi::c_ulong'}, {'name': 'nonresident_age', 'type': 'atomic_long_t'}, {'name': 'refaults', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'zswap_lruvec_state', 'type': 'zswap_lruvec_state'}]`

### Rust Evidence

- Graph edges: `4`

## W-001894 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: address_space
- Explanation: address_space changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'host', 'type': '*mut inode'}, {'name': 'i_pages', 'type': 'xarray'}, {'name': 'invalidate_lock', 'type': 'rw_semaphore'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'i_mmap_writable', 'type': 'atomic_t'}, {'name': 'i_mmap', 'type': 'rb_root_cached'}, {'name': 'nrpages', 'type': 'core::ffi::c_ulong'}, {'name': 'writeback_index', 'type': 'core::ffi::c_ulong'}, {'name': 'a_ops', 'type': '*const address_space_operations'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'i_mmap_rwsem', 'type': 'rw_semaphore'}, {'name': 'wb_err', 'type': 'errseq_t'}, {'name': 'private_lock', 'type': 'spinlock_t'}, {'name': 'private_list', 'type': 'list_head'}, {'name': 'private_data', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'host', 'type': '*mut inode'}, {'name': 'i_pages', 'type': 'xarray'}, {'name': 'invalidate_lock', 'type': 'rw_semaphore'}, {'name': 'gfp_mask', 'type': 'gfp_t'}, {'name': 'i_mmap_writable', 'type': 'atomic_t'}, {'name': 'i_mmap', 'type': 'rb_root_cached'}, {'name': 'nrpages', 'type': 'core::ffi::c_ulong'}, {'name': 'writeback_index', 'type': 'core::ffi::c_ulong'}, {'name': 'a_ops', 'type': '*const address_space_operations'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'i_mmap_rwsem', 'type': 'rw_semaphore'}, {'name': 'wb_err', 'type': 'errseq_t'}, {'name': 'i_private_lock', 'type': 'spinlock_t'}, {'name': 'i_private_list', 'type': 'list_head'}, {'name': 'i_private_data', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `3`

## W-001917 FieldDrift

- Risk: Medium
- Score: 9.2
- Symbol: resource
- Explanation: resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'start', 'type': 'resource_size_t'}, {'name': 'end', 'type': 'resource_size_t'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'desc', 'type': 'core::ffi::c_ulong'}, {'name': 'parent', 'type': '*mut resource'}, {'name': 'sibling', 'type': '*mut resource'}, {'name': 'child', 'type': '*mut resource'}]`

### Rust Evidence

- Graph edges: `3`

## W-001910 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: mem_section_usage
- Explanation: mem_section_usage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'subsection_map', 'type': '[core::ffi::c_ulong; 1usize]'}, {'name': 'pageblock_flags', 'type': '__IncompleteArrayField<core::ffi::c_ulong>'}]`
- New: `[{'name': 'rcu', 'type': 'callback_head'}, {'name': 'subsection_map', 'type': '[core::ffi::c_ulong; 1usize]'}, {'name': 'pageblock_flags', 'type': '__IncompleteArrayField<core::ffi::c_ulong>'}]`

### Rust Evidence

- Graph edges: `2`

## W-001912 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: nsproxy
- Explanation: nsproxy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'count', 'type': 'refcount_t'}, {'name': 'uts_ns', 'type': '*mut uts_namespace'}, {'name': 'ipc_ns', 'type': '*mut ipc_namespace'}, {'name': 'mnt_ns', 'type': '*mut mnt_namespace'}, {'name': 'pid_ns_for_children', 'type': '*mut pid_namespace'}, {'name': 'net_ns', 'type': '*mut net'}, {'name': 'time_ns', 'type': '*mut time_namespace'}, {'name': 'time_ns_for_children', 'type': '*mut time_namespace'}, {'name': 'cgroup_ns', 'type': '*mut cgroup_namespace'}]`

### Rust Evidence

- Graph edges: `2`

## W-001916 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: ptdesc
- Explanation: ptdesc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__page_flags', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'ptdesc__bindgen_ty_1'}, {'name': '__page_mapping', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'ptdesc__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'ptdesc__bindgen_ty_3'}, {'name': '__page_type', 'type': 'core::ffi::c_uint'}, {'name': '_refcount', 'type': 'atomic_t'}]`
- New: `[{'name': '__page_flags', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_1', 'type': 'ptdesc__bindgen_ty_1'}, {'name': '__page_mapping', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'ptdesc__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'ptdesc__bindgen_ty_3'}, {'name': '__page_type', 'type': 'core::ffi::c_uint'}, {'name': '__page_refcount', 'type': 'atomic_t'}]`

### Rust Evidence

- Graph edges: `2`

## W-001895 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: address_space_operations
- Explanation: address_space_operations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'writepage', 'type': '::core::option::Option<'}, {'name': 'read_folio', 'type': '::core::option::Option<'}, {'name': 'writepages', 'type': '::core::option::Option<'}, {'name': 'dirty_folio', 'type': '::core::option::Option<'}, {'name': 'readahead', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut readahead_control)>'}, {'name': 'write_begin', 'type': '::core::option::Option<'}, {'name': 'write_end', 'type': '::core::option::Option<'}, {'name': 'bmap', 'type': '::core::option::Option<'}, {'name': 'free_folio', 'type': '::core::option::Option<unsafe extern "C" fn(folio: *mut folio)>'}, {'name': 'direct_IO', 'type': '::core::option::Option<'}, {'name': 'migrate_folio', 'type': '::core::option::Option<'}, {'name': 'is_partially_uptodate', 'type': '::core::option::Option<'}, {'name': 'is_dirty_writeback', 'type': '::core::option::Option<'}, {'name': 'error_remove_page', 'type': '::core::option::Option<'}, {'name': 'swap_activate', 'type': '::core::option::Option<'}, {'name': 'swap_deactivate', 'type': '::core::option::Option<unsafe extern "C" fn(file: *mut file)>'}, {'name': 'swap_rw', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'writepage', 'type': '::core::option::Option<'}, {'name': 'read_folio', 'type': '::core::option::Option<'}, {'name': 'writepages', 'type': '::core::option::Option<'}, {'name': 'dirty_folio', 'type': '::core::option::Option<'}, {'name': 'readahead', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut readahead_control)>'}, {'name': 'write_begin', 'type': '::core::option::Option<'}, {'name': 'write_end', 'type': '::core::option::Option<'}, {'name': 'bmap', 'type': '::core::option::Option<'}, {'name': 'free_folio', 'type': '::core::option::Option<unsafe extern "C" fn(folio: *mut folio)>'}, {'name': 'direct_IO', 'type': '::core::option::Option<'}, {'name': 'migrate_folio', 'type': '::core::option::Option<'}, {'name': 'is_partially_uptodate', 'type': '::core::option::Option<'}, {'name': 'is_dirty_writeback', 'type': '::core::option::Option<'}, {'name': 'error_remove_folio', 'type': '::core::option::Option<'}, {'name': 'swap_activate', 'type': '::core::option::Option<'}, {'name': 'swap_deactivate', 'type': '::core::option::Option<unsafe extern "C" fn(file: *mut file)>'}, {'name': 'swap_rw', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-001897 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bio_vec
- Explanation: bio_vec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'bv_page', 'type': '*mut page'}, {'name': 'bv_len', 'type': 'core::ffi::c_uint'}, {'name': 'bv_offset', 'type': 'core::ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-001898 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: callthunk_sites
- Explanation: callthunk_sites changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'call_start', 'type': '*mut s32'}, {'name': 'call_end', 'type': '*mut s32'}, {'name': 'pv_start', 'type': '*mut paravirt_patch_site'}, {'name': 'pv_end', 'type': '*mut paravirt_patch_site'}]`
- New: `[{'name': 'call_start', 'type': '*mut s32'}, {'name': 'call_end', 'type': '*mut s32'}, {'name': 'alt_start', 'type': '*mut alt_instr'}, {'name': 'alt_end', 'type': '*mut alt_instr'}]`

### Rust Evidence

- Graph edges: `1`

## W-001899 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: compat_mmsghdr
- Explanation: compat_mmsghdr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'msg_hdr', 'type': 'compat_msghdr'}, {'name': 'msg_len', 'type': 'compat_uint_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-001900 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: compat_msghdr
- Explanation: compat_msghdr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'msg_name', 'type': 'compat_uptr_t'}, {'name': 'msg_namelen', 'type': 'compat_int_t'}, {'name': 'msg_iov', 'type': 'compat_uptr_t'}, {'name': 'msg_iovlen', 'type': 'compat_size_t'}, {'name': 'msg_control', 'type': 'compat_uptr_t'}, {'name': 'msg_controllen', 'type': 'compat_size_t'}, {'name': 'msg_flags', 'type': 'compat_uint_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-001903 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: dev_printk_info
- Explanation: dev_printk_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'subsystem', 'type': '[core::ffi::c_char; 16usize]'}, {'name': 'device', 'type': '[core::ffi::c_char; 48usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-001908 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ma_state
- Explanation: ma_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'tree', 'type': '*mut maple_tree'}, {'name': 'index', 'type': 'core::ffi::c_ulong'}, {'name': 'last', 'type': 'core::ffi::c_ulong'}, {'name': 'node', 'type': '*mut maple_enode'}, {'name': 'min', 'type': 'core::ffi::c_ulong'}, {'name': 'max', 'type': 'core::ffi::c_ulong'}, {'name': 'alloc', 'type': '*mut maple_alloc'}, {'name': 'depth', 'type': 'core::ffi::c_uchar'}, {'name': 'offset', 'type': 'core::ffi::c_uchar'}, {'name': 'mas_flags', 'type': 'core::ffi::c_uchar'}]`
- New: `[{'name': 'tree', 'type': '*mut maple_tree'}, {'name': 'index', 'type': 'core::ffi::c_ulong'}, {'name': 'last', 'type': 'core::ffi::c_ulong'}, {'name': 'node', 'type': '*mut maple_enode'}, {'name': 'min', 'type': 'core::ffi::c_ulong'}, {'name': 'max', 'type': 'core::ffi::c_ulong'}, {'name': 'alloc', 'type': '*mut maple_alloc'}, {'name': 'status', 'type': 'maple_status'}, {'name': 'depth', 'type': 'core::ffi::c_uchar'}, {'name': 'offset', 'type': 'core::ffi::c_uchar'}, {'name': 'mas_flags', 'type': 'core::ffi::c_uchar'}, {'name': 'end', 'type': 'core::ffi::c_uchar'}]`

### Rust Evidence

- Graph edges: `1`

## W-001909 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ma_wr_state
- Explanation: ma_wr_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mas', 'type': '*mut ma_state'}, {'name': 'node', 'type': '*mut maple_node'}, {'name': 'r_min', 'type': 'core::ffi::c_ulong'}, {'name': 'r_max', 'type': 'core::ffi::c_ulong'}, {'name': 'type_', 'type': 'maple_type'}, {'name': 'offset_end', 'type': 'core::ffi::c_uchar'}, {'name': 'node_end', 'type': 'core::ffi::c_uchar'}, {'name': 'pivots', 'type': '*mut core::ffi::c_ulong'}, {'name': 'end_piv', 'type': 'core::ffi::c_ulong'}, {'name': 'slots', 'type': '*mut *mut core::ffi::c_void'}, {'name': 'entry', 'type': '*mut core::ffi::c_void'}, {'name': 'content', 'type': '*mut core::ffi::c_void'}]`
- New: `[{'name': 'mas', 'type': '*mut ma_state'}, {'name': 'node', 'type': '*mut maple_node'}, {'name': 'r_min', 'type': 'core::ffi::c_ulong'}, {'name': 'r_max', 'type': 'core::ffi::c_ulong'}, {'name': 'type_', 'type': 'maple_type'}, {'name': 'offset_end', 'type': 'core::ffi::c_uchar'}, {'name': 'pivots', 'type': '*mut core::ffi::c_ulong'}, {'name': 'end_piv', 'type': 'core::ffi::c_ulong'}, {'name': 'slots', 'type': '*mut *mut core::ffi::c_void'}, {'name': 'entry', 'type': '*mut core::ffi::c_void'}, {'name': 'content', 'type': '*mut core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `1`

## W-001911 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: name_snapshot
- Explanation: name_snapshot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': 'qstr'}, {'name': 'inline_name', 'type': '[core::ffi::c_uchar; 32usize]'}]`
- New: `[{'name': 'name', 'type': 'qstr'}, {'name': 'inline_name', 'type': '[core::ffi::c_uchar; 40usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-001913 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: page__bindgen_ty_1__bindgen_ty_2
- Explanation: page__bindgen_ty_1__bindgen_ty_2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'pp_magic', 'type': 'core::ffi::c_ulong'}, {'name': 'pp', 'type': '*mut page_pool'}, {'name': '_pp_mapping_pad', 'type': 'core::ffi::c_ulong'}, {'name': 'dma_addr', 'type': 'core::ffi::c_ulong'}, {'name': 'pp_frag_count', 'type': 'atomic_long_t'}]`
- New: `[{'name': 'pp_magic', 'type': 'core::ffi::c_ulong'}, {'name': 'pp', 'type': '*mut page_pool'}, {'name': '_pp_mapping_pad', 'type': 'core::ffi::c_ulong'}, {'name': 'dma_addr', 'type': 'core::ffi::c_ulong'}, {'name': 'pp_ref_count', 'type': 'atomic_long_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-001914 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: per_cpu_nodestat
- Explanation: per_cpu_nodestat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_node_stat_diff', 'type': '[s8; 41usize]'}]`
- New: `[{'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_node_stat_diff', 'type': '[s8; 44usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-001915 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: pglist_data
- Explanation: pglist_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'node_zones', 'type': '[zone; 4usize]'}, {'name': 'node_zonelists', 'type': '[zonelist; 2usize]'}, {'name': 'nr_zones', 'type': 'core::ffi::c_int'}, {'name': 'node_start_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'node_present_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'node_spanned_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'node_id', 'type': 'core::ffi::c_int'}, {'name': 'kswapd_wait', 'type': 'wait_queue_head_t'}, {'name': 'pfmemalloc_wait', 'type': 'wait_queue_head_t'}, {'name': 'reclaim_wait', 'type': '[wait_queue_head_t; 4usize]'}, {'name': 'nr_writeback_throttled', 'type': 'atomic_t'}, {'name': 'nr_reclaim_start', 'type': 'core::ffi::c_ulong'}, {'name': 'kswapd', 'type': '*mut task_struct'}, {'name': 'kswapd_order', 'type': 'core::ffi::c_int'}, {'name': 'kswapd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kswapd_failures', 'type': 'core::ffi::c_int'}, {'name': 'kcompactd_max_order', 'type': 'core::ffi::c_int'}, {'name': 'kcompactd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kcompactd_wait', 'type': 'wait_queue_head_t'}, {'name': 'kcompactd', 'type': '*mut task_struct'}, {'name': 'proactive_compact_trigger', 'type': 'bool_'}, {'name': 'totalreserve_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'min_unmapped_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'min_slab_pages', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': '__lruvec', 'type': 'lruvec'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'per_cpu_nodestats', 'type': '*mut per_cpu_nodestat'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 41usize]'}, {'name': 'memtier', 'type': '*mut memory_tier'}]`
- New: `[{'name': 'node_zones', 'type': '[zone; 4usize]'}, {'name': 'node_zonelists', 'type': '[zonelist; 2usize]'}, {'name': 'nr_zones', 'type': 'core::ffi::c_int'}, {'name': 'node_start_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'node_present_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'node_spanned_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'node_id', 'type': 'core::ffi::c_int'}, {'name': 'kswapd_wait', 'type': 'wait_queue_head_t'}, {'name': 'pfmemalloc_wait', 'type': 'wait_queue_head_t'}, {'name': 'reclaim_wait', 'type': '[wait_queue_head_t; 4usize]'}, {'name': 'nr_writeback_throttled', 'type': 'atomic_t'}, {'name': 'nr_reclaim_start', 'type': 'core::ffi::c_ulong'}, {'name': 'kswapd', 'type': '*mut task_struct'}, {'name': 'kswapd_order', 'type': 'core::ffi::c_int'}, {'name': 'kswapd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kswapd_failures', 'type': 'core::ffi::c_int'}, {'name': 'kcompactd_max_order', 'type': 'core::ffi::c_int'}, {'name': 'kcompactd_highest_zoneidx', 'type': 'zone_type'}, {'name': 'kcompactd_wait', 'type': 'wait_queue_head_t'}, {'name': 'kcompactd', 'type': '*mut task_struct'}, {'name': 'proactive_compact_trigger', 'type': 'bool_'}, {'name': 'totalreserve_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'min_unmapped_pages', 'type': 'core::ffi::c_ulong'}, {'name': 'min_slab_pages', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': '__lruvec', 'type': 'lruvec'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_1', 'type': '[u64; 6usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'per_cpu_nodestats', 'type': '*mut per_cpu_nodestat'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 44usize]'}, {'name': 'memtier', 'type': '*mut memory_tier'}]`

### Rust Evidence

- Graph edges: `1`

## W-001918 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sb_writers
- Explanation: sb_writers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'frozen', 'type': 'core::ffi::c_ushort'}, {'name': 'freeze_holders', 'type': 'core::ffi::c_ushort'}, {'name': 'rw_sem', 'type': '[percpu_rw_semaphore; 3usize]'}]`
- New: `[{'name': 'frozen', 'type': 'core::ffi::c_ushort'}, {'name': 'freeze_kcount', 'type': 'core::ffi::c_int'}, {'name': 'freeze_ucount', 'type': 'core::ffi::c_int'}, {'name': 'rw_sem', 'type': '[percpu_rw_semaphore; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-001919 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_avg
- Explanation: sched_avg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'last_update_time', 'type': 'u64_'}, {'name': 'load_sum', 'type': 'u64_'}, {'name': 'runnable_sum', 'type': 'u64_'}, {'name': 'util_sum', 'type': 'u32_'}, {'name': 'period_contrib', 'type': 'u32_'}, {'name': 'load_avg', 'type': 'core::ffi::c_ulong'}, {'name': 'runnable_avg', 'type': 'core::ffi::c_ulong'}, {'name': 'util_avg', 'type': 'core::ffi::c_ulong'}, {'name': 'util_est', 'type': 'util_est'}]`
- New: `[{'name': 'last_update_time', 'type': 'u64_'}, {'name': 'load_sum', 'type': 'u64_'}, {'name': 'runnable_sum', 'type': 'u64_'}, {'name': 'util_sum', 'type': 'u32_'}, {'name': 'period_contrib', 'type': 'u32_'}, {'name': 'load_avg', 'type': 'core::ffi::c_ulong'}, {'name': 'runnable_avg', 'type': 'core::ffi::c_ulong'}, {'name': 'util_avg', 'type': 'core::ffi::c_ulong'}, {'name': 'util_est', 'type': 'core::ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-001920 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_dl_entity
- Explanation: sched_dl_entity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'rb_node', 'type': 'rb_node'}, {'name': 'dl_runtime', 'type': 'u64_'}, {'name': 'dl_deadline', 'type': 'u64_'}, {'name': 'dl_period', 'type': 'u64_'}, {'name': 'dl_bw', 'type': 'u64_'}, {'name': 'dl_density', 'type': 'u64_'}, {'name': 'runtime', 'type': 's64'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'dl_timer', 'type': 'hrtimer'}, {'name': 'inactive_timer', 'type': 'hrtimer'}, {'name': 'pi_se', 'type': '*mut sched_dl_entity'}]`
- New: `[{'name': 'rb_node', 'type': 'rb_node'}, {'name': 'dl_runtime', 'type': 'u64_'}, {'name': 'dl_deadline', 'type': 'u64_'}, {'name': 'dl_period', 'type': 'u64_'}, {'name': 'dl_bw', 'type': 'u64_'}, {'name': 'dl_density', 'type': 'u64_'}, {'name': 'runtime', 'type': 's64'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'flags', 'type': 'core::ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'dl_timer', 'type': 'hrtimer'}, {'name': 'inactive_timer', 'type': 'hrtimer'}, {'name': 'rq', 'type': '*mut rq'}, {'name': 'server_has_tasks', 'type': 'dl_server_has_tasks_f'}, {'name': 'server_pick', 'type': 'dl_server_pick_f'}, {'name': 'pi_se', 'type': '*mut sched_dl_entity'}]`

### Rust Evidence

- Graph edges: `1`

## W-001921 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_entity
- Explanation: sched_entity changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'load', 'type': 'load_weight'}, {'name': 'run_node', 'type': 'rb_node'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'min_deadline', 'type': 'u64_'}, {'name': 'group_node', 'type': 'list_head'}, {'name': 'on_rq', 'type': 'core::ffi::c_uint'}, {'name': 'exec_start', 'type': 'u64_'}, {'name': 'sum_exec_runtime', 'type': 'u64_'}, {'name': 'prev_sum_exec_runtime', 'type': 'u64_'}, {'name': 'vruntime', 'type': 'u64_'}, {'name': 'vlag', 'type': 's64'}, {'name': 'slice', 'type': 'u64_'}, {'name': 'nr_migrations', 'type': 'u64_'}, {'name': 'depth', 'type': 'core::ffi::c_int'}, {'name': 'parent', 'type': '*mut sched_entity'}, {'name': 'cfs_rq', 'type': '*mut cfs_rq'}, {'name': 'my_q', 'type': '*mut cfs_rq'}, {'name': 'runnable_weight', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 2usize]'}, {'name': 'avg', 'type': 'sched_avg'}]`
- New: `[{'name': 'load', 'type': 'load_weight'}, {'name': 'run_node', 'type': 'rb_node'}, {'name': 'deadline', 'type': 'u64_'}, {'name': 'min_vruntime', 'type': 'u64_'}, {'name': 'group_node', 'type': 'list_head'}, {'name': 'on_rq', 'type': 'core::ffi::c_uint'}, {'name': 'exec_start', 'type': 'u64_'}, {'name': 'sum_exec_runtime', 'type': 'u64_'}, {'name': 'prev_sum_exec_runtime', 'type': 'u64_'}, {'name': 'vruntime', 'type': 'u64_'}, {'name': 'vlag', 'type': 's64'}, {'name': 'slice', 'type': 'u64_'}, {'name': 'nr_migrations', 'type': 'u64_'}, {'name': 'depth', 'type': 'core::ffi::c_int'}, {'name': 'parent', 'type': '*mut sched_entity'}, {'name': 'cfs_rq', 'type': '*mut cfs_rq'}, {'name': 'my_q', 'type': '*mut cfs_rq'}, {'name': 'runnable_weight', 'type': 'core::ffi::c_ulong'}, {'name': '__bindgen_padding_0', 'type': '[u64; 2usize]'}, {'name': 'avg', 'type': 'sched_avg'}]`

### Rust Evidence

- Graph edges: `1`

## W-001922 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sched_statistics
- Explanation: sched_statistics changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'wait_start', 'type': 'u64_'}, {'name': 'wait_max', 'type': 'u64_'}, {'name': 'wait_count', 'type': 'u64_'}, {'name': 'wait_sum', 'type': 'u64_'}, {'name': 'iowait_count', 'type': 'u64_'}, {'name': 'iowait_sum', 'type': 'u64_'}, {'name': 'sleep_start', 'type': 'u64_'}, {'name': 'sleep_max', 'type': 'u64_'}, {'name': 'sum_sleep_runtime', 'type': 's64'}, {'name': 'block_start', 'type': 'u64_'}, {'name': 'block_max', 'type': 'u64_'}, {'name': 'sum_block_runtime', 'type': 's64'}, {'name': 'exec_max', 'type': 'u64_'}, {'name': 'slice_max', 'type': 'u64_'}, {'name': 'nr_migrations_cold', 'type': 'u64_'}, {'name': 'nr_failed_migrations_affine', 'type': 'u64_'}, {'name': 'nr_failed_migrations_running', 'type': 'u64_'}, {'name': 'nr_failed_migrations_hot', 'type': 'u64_'}, {'name': 'nr_forced_migrations', 'type': 'u64_'}, {'name': 'nr_wakeups', 'type': 'u64_'}, {'name': 'nr_wakeups_sync', 'type': 'u64_'}, {'name': 'nr_wakeups_migrate', 'type': 'u64_'}, {'name': 'nr_wakeups_local', 'type': 'u64_'}, {'name': 'nr_wakeups_remote', 'type': 'u64_'}, {'name': 'nr_wakeups_affine', 'type': 'u64_'}, {'name': 'nr_wakeups_affine_attempts', 'type': 'u64_'}, {'name': 'nr_wakeups_passive', 'type': 'u64_'}, {'name': 'nr_wakeups_idle', 'type': 'u64_'}]`
- New: `[{'name': 'wait_start', 'type': 'u64_'}, {'name': 'wait_max', 'type': 'u64_'}, {'name': 'wait_count', 'type': 'u64_'}, {'name': 'wait_sum', 'type': 'u64_'}, {'name': 'iowait_count', 'type': 'u64_'}, {'name': 'iowait_sum', 'type': 'u64_'}, {'name': 'sleep_start', 'type': 'u64_'}, {'name': 'sleep_max', 'type': 'u64_'}, {'name': 'sum_sleep_runtime', 'type': 's64'}, {'name': 'block_start', 'type': 'u64_'}, {'name': 'block_max', 'type': 'u64_'}, {'name': 'sum_block_runtime', 'type': 's64'}, {'name': 'exec_max', 'type': 's64'}, {'name': 'slice_max', 'type': 'u64_'}, {'name': 'nr_migrations_cold', 'type': 'u64_'}, {'name': 'nr_failed_migrations_affine', 'type': 'u64_'}, {'name': 'nr_failed_migrations_running', 'type': 'u64_'}, {'name': 'nr_failed_migrations_hot', 'type': 'u64_'}, {'name': 'nr_forced_migrations', 'type': 'u64_'}, {'name': 'nr_wakeups', 'type': 'u64_'}, {'name': 'nr_wakeups_sync', 'type': 'u64_'}, {'name': 'nr_wakeups_migrate', 'type': 'u64_'}, {'name': 'nr_wakeups_local', 'type': 'u64_'}, {'name': 'nr_wakeups_remote', 'type': 'u64_'}, {'name': 'nr_wakeups_affine', 'type': 'u64_'}, {'name': 'nr_wakeups_affine_attempts', 'type': 'u64_'}, {'name': 'nr_wakeups_passive', 'type': 'u64_'}, {'name': 'nr_wakeups_idle', 'type': 'u64_'}]`

### Rust Evidence

- Graph edges: `1`

## W-001923 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sg_table
- Explanation: sg_table changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'sgl', 'type': '*mut scatterlist'}, {'name': 'nents', 'type': 'core::ffi::c_uint'}, {'name': 'orig_nents', 'type': 'core::ffi::c_uint'}]`

### Rust Evidence

- Graph edges: `1`

## W-001926 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_block
- Explanation: super_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'core::ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'core::ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'core::ffi::c_ulong'}, {'name': 's_iflags', 'type': 'core::ffi::c_ulong'}, {'name': 's_magic', 'type': 'core::ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'core::ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut core::ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_handle', 'type': '*mut bdev_handle'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'core::ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut core::ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': '__u32'}, {'name': 's_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 's_id', 'type': '[core::ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_max_links', 'type': 'core::ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const core::ffi::c_char'}, {'name': 's_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_fsnotify_connectors', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'core::ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 11usize]'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`
- New: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'core::ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'core::ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'core::ffi::c_ulong'}, {'name': 's_iflags', 'type': 'core::ffi::c_ulong'}, {'name': 's_magic', 'type': 'core::ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'core::ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut core::ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_handle', 'type': '*mut bdev_handle'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'core::ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut core::ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': '__u32'}, {'name': 's_fsnotify_marks', 'type': '*mut fsnotify_mark_connector'}, {'name': 's_id', 'type': '[core::ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_max_links', 'type': 'core::ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const core::ffi::c_char'}, {'name': 's_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_fsnotify_connectors', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'core::ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'core::ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 9usize]'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-001930 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_operations_struct
- Explanation: vm_operations_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'open', 'type': '::core::option::Option<unsafe extern "C" fn(area: *mut vm_area_struct)>'}, {'name': 'close', 'type': '::core::option::Option<unsafe extern "C" fn(area: *mut vm_area_struct)>'}, {'name': 'may_split', 'type': '::core::option::Option<'}, {'name': 'mprotect', 'type': '::core::option::Option<'}, {'name': 'fault', 'type': '::core::option::Option<unsafe extern "C" fn(vmf: *mut vm_fault) -> vm_fault_t>'}, {'name': 'huge_fault', 'type': '::core::option::Option<'}, {'name': 'map_pages', 'type': '::core::option::Option<'}, {'name': 'pagesize', 'type': '::core::option::Option<'}, {'name': 'pfn_mkwrite', 'type': '::core::option::Option<unsafe extern "C" fn(vmf: *mut vm_fault) -> vm_fault_t>'}, {'name': 'access', 'type': '::core::option::Option<'}, {'name': 'name', 'type': '::core::option::Option<'}, {'name': 'set_policy', 'type': '::core::option::Option<'}, {'name': 'get_policy', 'type': '::core::option::Option<'}, {'name': 'find_special_page', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-001931 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vm_struct
- Explanation: vm_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'next', 'type': '*mut vm_struct'}, {'name': 'addr', 'type': '*mut core::ffi::c_void'}, {'name': 'size', 'type': 'core::ffi::c_ulong'}, {'name': 'flags', 'type': 'core::ffi::c_ulong'}, {'name': 'pages', 'type': '*mut *mut page'}, {'name': 'page_order', 'type': 'core::ffi::c_uint'}, {'name': 'nr_pages', 'type': 'core::ffi::c_uint'}, {'name': 'phys_addr', 'type': 'phys_addr_t'}, {'name': 'caller', 'type': '*const core::ffi::c_void'}]`

### Rust Evidence

- Graph edges: `1`

## W-001932 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vma_numab_state
- Explanation: vma_numab_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'next_scan', 'type': 'core::ffi::c_ulong'}, {'name': 'pids_active_reset', 'type': 'core::ffi::c_ulong'}, {'name': 'pids_active', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'prev_scan_seq', 'type': 'core::ffi::c_int'}]`
- New: `[{'name': 'next_scan', 'type': 'core::ffi::c_ulong'}, {'name': 'pids_active_reset', 'type': 'core::ffi::c_ulong'}, {'name': 'pids_active', 'type': '[core::ffi::c_ulong; 2usize]'}, {'name': 'start_scan_seq', 'type': 'core::ffi::c_int'}, {'name': 'prev_scan_seq', 'type': 'core::ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-001933 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: vmem_altmap
- Explanation: vmem_altmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'base_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'end_pfn', 'type': 'core::ffi::c_ulong'}, {'name': 'reserve', 'type': 'core::ffi::c_ulong'}, {'name': 'free', 'type': 'core::ffi::c_ulong'}, {'name': 'align', 'type': 'core::ffi::c_ulong'}, {'name': 'alloc', 'type': 'core::ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-001934 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: CONFIG_RUSTC_VERSION_TEXT
- Explanation: CONFIG_RUSTC_VERSION_TEXT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `b"rustc 1.73.0 (cc66ad468 2023-10-03)\0"`
- New: `b"rustc 1.74.1 (a28077b28 2023-12-04)\0"`

### Rust Evidence

- Graph edges: `1`

## W-001935 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: DNAME_INLINE_LEN
- Explanation: DNAME_INLINE_LEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-001936 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: IA32_NR_syscalls
- Explanation: IA32_NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `457`
- New: `462`

### Rust Evidence

- Graph edges: `1`

## W-001937 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NR_syscalls
- Explanation: NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `457`
- New: `462`

### Rust Evidence

- Graph edges: `1`

## W-001938 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_ia32_syscalls
- Explanation: __NR_ia32_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `457`
- New: `462`

### Rust Evidence

- Graph edges: `1`

## W-001939 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: __NR_syscalls
- Explanation: __NR_syscalls changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `457`
- New: `462`

### Rust Evidence

- Graph edges: `1`

## W-001940 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: node_stat_item_NR_VM_NODE_STAT_ITEMS
- Explanation: node_stat_item_NR_VM_NODE_STAT_ITEMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-001941 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: KMALLOC_SHIFT_MAX
- Explanation: KMALLOC_SHIFT_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(MAX_ORDER + PAGE_SHIFT)`
- New: `(MAX_PAGE_ORDER + PAGE_SHIFT)`

### Rust Evidence

- Graph edges: `1`
