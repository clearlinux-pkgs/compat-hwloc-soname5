#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-hwloc-soname5
Version  : 1.11.3
Release  : 7
URL      : https://www.open-mpi.org/software/hwloc/v1.11/downloads/hwloc-1.11.3.tar.gz
Source0  : https://www.open-mpi.org/software/hwloc/v1.11/downloads/hwloc-1.11.3.tar.gz
Summary  : Hardware locality detection and management library
Group    : Development/Tools
License  : Intel
Requires: compat-hwloc-soname5-lib = %{version}-%{release}
Requires: compat-hwloc-soname5-license = %{version}-%{release}
BuildRequires : cairo-dev
BuildRequires : doxygen
BuildRequires : libpciaccess-dev
BuildRequires : libxml2-dev
BuildRequires : ncurses-dev
BuildRequires : numactl-dev
BuildRequires : pciutils-dev
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(x11)
BuildRequires : systemd-dev
BuildRequires : valgrind
# Suppress generation of debuginfo
%global debug_package %{nil}

%description
Introduction
hwloc provides command line tools and a C API to obtain the hierarchical map of
key computing elements, such as: NUMA memory nodes, shared caches, processor
packages, processor cores, processing units (logical processors or "threads")
and even I/O devices. hwloc also gathers various attributes such as cache and
memory information, and is portable across a variety of different operating
systems and platforms. Additionally it may assemble the topologies of multiple
machines into a single one so as to let applications consult the topology of an
entire fabric or cluster at once.

%package lib
Summary: lib components for the compat-hwloc-soname5 package.
Group: Libraries
Requires: compat-hwloc-soname5-license = %{version}-%{release}

%description lib
lib components for the compat-hwloc-soname5 package.


%package license
Summary: license components for the compat-hwloc-soname5 package.
Group: Default

%description license
license components for the compat-hwloc-soname5 package.


%prep
%setup -q -n hwloc-1.11.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567810163
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1567810163
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-hwloc-soname5
cp COPYING %{buildroot}/usr/share/package-licenses/compat-hwloc-soname5/COPYING
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/hwloc-annotate
rm -f %{buildroot}/usr/bin/hwloc-assembler
rm -f %{buildroot}/usr/bin/hwloc-assembler-remote
rm -f %{buildroot}/usr/bin/hwloc-bind
rm -f %{buildroot}/usr/bin/hwloc-calc
rm -f %{buildroot}/usr/bin/hwloc-compress-dir
rm -f %{buildroot}/usr/bin/hwloc-diff
rm -f %{buildroot}/usr/bin/hwloc-distances
rm -f %{buildroot}/usr/bin/hwloc-distrib
rm -f %{buildroot}/usr/bin/hwloc-dump-hwdata
rm -f %{buildroot}/usr/bin/hwloc-gather-topology
rm -f %{buildroot}/usr/bin/hwloc-info
rm -f %{buildroot}/usr/bin/hwloc-ls
rm -f %{buildroot}/usr/bin/hwloc-patch
rm -f %{buildroot}/usr/bin/hwloc-ps
rm -f %{buildroot}/usr/bin/lstopo
rm -f %{buildroot}/usr/bin/lstopo-no-graphics
rm -f %{buildroot}/usr/include/hwloc.h
rm -f %{buildroot}/usr/include/hwloc/autogen/config.h
rm -f %{buildroot}/usr/include/hwloc/bitmap.h
rm -f %{buildroot}/usr/include/hwloc/cuda.h
rm -f %{buildroot}/usr/include/hwloc/cudart.h
rm -f %{buildroot}/usr/include/hwloc/deprecated.h
rm -f %{buildroot}/usr/include/hwloc/diff.h
rm -f %{buildroot}/usr/include/hwloc/gl.h
rm -f %{buildroot}/usr/include/hwloc/glibc-sched.h
rm -f %{buildroot}/usr/include/hwloc/helper.h
rm -f %{buildroot}/usr/include/hwloc/inlines.h
rm -f %{buildroot}/usr/include/hwloc/intel-mic.h
rm -f %{buildroot}/usr/include/hwloc/linux-libnuma.h
rm -f %{buildroot}/usr/include/hwloc/linux.h
rm -f %{buildroot}/usr/include/hwloc/myriexpress.h
rm -f %{buildroot}/usr/include/hwloc/nvml.h
rm -f %{buildroot}/usr/include/hwloc/opencl.h
rm -f %{buildroot}/usr/include/hwloc/openfabrics-verbs.h
rm -f %{buildroot}/usr/include/hwloc/plugins.h
rm -f %{buildroot}/usr/include/hwloc/rename.h
rm -f %{buildroot}/usr/lib64/libhwloc.so
rm -f %{buildroot}/usr/lib64/pkgconfig/hwloc.pc
rm -f %{buildroot}/usr/share/applications/lstopo.desktop
rm -f %{buildroot}/usr/share/doc/hwloc/hwloc-a4.pdf
rm -f %{buildroot}/usr/share/doc/hwloc/hwloc-letter.pdf
rm -f %{buildroot}/usr/share/hwloc/hwloc-dump-hwdata.service
rm -f %{buildroot}/usr/share/hwloc/hwloc-valgrind.supp
rm -f %{buildroot}/usr/share/hwloc/hwloc.dtd
rm -f %{buildroot}/usr/share/man/man1/hwloc-annotate.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-assembler-remote.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-assembler.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-bind.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-calc.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-compress-dir.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-diff.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-distances.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-distrib.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-dump-hwdata.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-gather-topology.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-info.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-ls.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-patch.1
rm -f %{buildroot}/usr/share/man/man1/hwloc-ps.1
rm -f %{buildroot}/usr/share/man/man1/lstopo-no-graphics.1
rm -f %{buildroot}/usr/share/man/man1/lstopo.1
rm -f %{buildroot}/usr/share/man/man3/HWLOC_API_VERSION.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_CPUBIND_NOMEMBIND.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_CPUBIND_PROCESS.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_CPUBIND_STRICT.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_CPUBIND_THREAD.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_DISTRIB_FLAG_REVERSE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_BIND.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_BYNODESET.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_DEFAULT.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_FIRSTTOUCH.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_INTERLEAVE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_MIGRATE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_MIXED.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_NEXTTOUCH.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_NOCPUBIND.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_PROCESS.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_REPLICATE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_STRICT.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_MEMBIND_THREAD.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_BRIDGE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_BRIDGE_HOST.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_BRIDGE_PCI.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_CACHE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_CACHE_DATA.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_CACHE_INSTRUCTION.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_CACHE_UNIFIED.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_CORE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_GROUP.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_MACHINE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_MISC.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_NUMANODE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_OSDEV_BLOCK.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_OSDEV_COPROC.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_OSDEV_DMA.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_OSDEV_GPU.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_OSDEV_NETWORK.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_OSDEV_OPENFABRICS.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_OS_DEVICE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_PACKAGE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_PCI_DEVICE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_PU.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_OBJ_SYSTEM.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_RESTRICT_FLAG_ADAPT_DISTANCES.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_RESTRICT_FLAG_ADAPT_IO.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_RESTRICT_FLAG_ADAPT_MISC.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TOPOLOGY_DIFF_APPLY_REVERSE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TOPOLOGY_DIFF_OBJ_ATTR.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TOPOLOGY_DIFF_OBJ_ATTR_INFO.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TOPOLOGY_DIFF_OBJ_ATTR_NAME.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TOPOLOGY_DIFF_OBJ_ATTR_SIZE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TOPOLOGY_DIFF_TOO_COMPLEX.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TOPOLOGY_FLAG_ICACHES.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TOPOLOGY_FLAG_IO_BRIDGES.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TOPOLOGY_FLAG_IO_DEVICES.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TOPOLOGY_FLAG_IS_THISSYSTEM.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TOPOLOGY_FLAG_WHOLE_IO.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TOPOLOGY_FLAG_WHOLE_SYSTEM.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TYPE_DEPTH_BRIDGE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TYPE_DEPTH_MULTIPLE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TYPE_DEPTH_OS_DEVICE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TYPE_DEPTH_PCI_DEVICE.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TYPE_DEPTH_UNKNOWN.3
rm -f %{buildroot}/usr/share/man/man3/HWLOC_TYPE_UNORDERED.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_alloc.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_alloc_membind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_alloc_membind_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_alloc_membind_policy.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_alloc_membind_policy_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_allbut.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_alloc.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_alloc_full.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_and.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_andnot.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_asprintf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_clr.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_clr_range.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_compare.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_compare_first.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_copy.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_dup.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_fill.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_first.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_foreach_begin.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_foreach_end.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_free.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_from_ith_ulong.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_from_ulong.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_intersects.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_isequal.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_isfull.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_isincluded.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_isset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_iszero.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_last.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_list_asprintf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_list_snprintf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_list_sscanf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_next.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_not.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_only.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_or.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_set.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_set_ith_ulong.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_set_range.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_singlify.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_snprintf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_sscanf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_taskset_asprintf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_taskset_snprintf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_taskset_sscanf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_to_ith_ulong.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_to_ulong.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_weight.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_xor.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bitmap_zero.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_bridge_covers_pcibus.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_compare_types.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_compare_types_e.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_const_bitmap_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_const_cpuset_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_const_nodeset_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cpubind_flags_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cpuset_from_glibc_sched_affinity.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cpuset_from_linux_libnuma_bitmask.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cpuset_from_linux_libnuma_ulongs.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cpuset_from_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cpuset_from_nodeset_strict.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cpuset_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cpuset_to_glibc_sched_affinity.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cpuset_to_linux_libnuma_bitmask.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cpuset_to_linux_libnuma_ulongs.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cpuset_to_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cpuset_to_nodeset_strict.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cuda_get_device_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cuda_get_device_osdev.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cuda_get_device_osdev_by_index.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cuda_get_device_pci_ids.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cuda_get_device_pcidev.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cudart_get_device_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cudart_get_device_osdev_by_index.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cudart_get_device_pci_ids.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_cudart_get_device_pcidev.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_custom_insert_group_object_by_parent.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_custom_insert_topology.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_distances_s.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_distrib.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_distrib_flags_e.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_export_obj_userdata.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_export_obj_userdata_base64.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_free.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_free_xmlbuffer.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_ancestor_obj_by_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_ancestor_obj_by_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_api_version.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_area_membind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_area_membind_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_area_memlocation.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_cache_covering_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_cache_type_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_child_covering_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_closest_objs.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_common_ancestor_obj.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_cpubind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_depth_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_distance_matrix_covering_obj_by_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_first_largest_obj_inside_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_hostbridge_by_pcibus.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_largest_objs_inside_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_last_cpu_location.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_latency.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_membind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_membind_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_nbobjs_by_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_nbobjs_by_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_nbobjs_inside_cpuset_by_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_nbobjs_inside_cpuset_by_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_next_bridge.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_next_child.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_next_obj_by_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_next_obj_by_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_next_obj_covering_cpuset_by_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_next_obj_covering_cpuset_by_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_next_obj_inside_cpuset_by_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_next_obj_inside_cpuset_by_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_next_osdev.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_next_pcidev.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_non_io_ancestor_obj.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_obj_below_array_by_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_obj_below_by_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_obj_by_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_obj_by_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_obj_covering_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_obj_index_inside_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_obj_inside_cpuset_by_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_obj_inside_cpuset_by_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_pcidev_by_busid.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_pcidev_by_busidstring.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_proc_cpubind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_proc_last_cpu_location.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_proc_membind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_proc_membind_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_pu_obj_by_os_index.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_root_obj.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_shared_cache_covering_obj.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_thread_cpubind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_type_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_type_depth_e.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_type_or_above_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_type_or_below_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_whole_distance_matrix_by_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_get_whole_distance_matrix_by_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_gl_get_display_by_osdev.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_gl_get_display_osdev_by_name.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_gl_get_display_osdev_by_port_device.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_ibv_get_device_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_ibv_get_device_osdev.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_ibv_get_device_osdev_by_name.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_intel_mic_get_device_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_intel_mic_get_device_osdev_by_index.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_linux_get_tid_cpubind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_linux_get_tid_last_cpu_location.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_linux_parse_cpumap_file.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_linux_set_tid_cpubind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_membind_flags_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_membind_policy_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_mx_board_get_device_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_mx_endpoint_get_device_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_nodeset_from_linux_libnuma_bitmask.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_nodeset_from_linux_libnuma_ulongs.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_nodeset_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_nodeset_to_linux_libnuma_bitmask.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_nodeset_to_linux_libnuma_ulongs.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_nvml_get_device_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_nvml_get_device_osdev.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_nvml_get_device_osdev_by_index.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_add_info.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_attr_snprintf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_attr_u.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_attr_u_hwloc_bridge_attr_s.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_attr_u_hwloc_cache_attr_s.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_attr_u_hwloc_group_attr_s.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_attr_u_hwloc_osdev_attr_s.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_attr_u_hwloc_pcidev_attr_s.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_bridge_type_e.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_bridge_type_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_cache_type_e.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_cache_type_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_cpuset_snprintf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_get_info_by_name.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_info_s.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_is_in_subtree.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_memory_s.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_memory_s_hwloc_obj_memory_page_type_s.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_osdev_type_e.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_osdev_type_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_type_snprintf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_type_sscanf.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_type_string.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_obj_type_t.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_opencl_get_device_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_opencl_get_device_osdev.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_opencl_get_device_osdev_by_index.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_restrict_flags_e.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_set_area_membind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_set_area_membind_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_set_cpubind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_set_membind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_set_membind_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_set_proc_cpubind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_set_proc_membind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_set_proc_membind_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_set_thread_cpubind.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_check.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_cpubind_support.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_destroy.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_diff_apply.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_diff_apply_flags_e.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_diff_build.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_diff_destroy.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_diff_export_xml.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_diff_export_xmlbuffer.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_diff_load_xml.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_diff_load_xmlbuffer.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_diff_obj_attr_type_e.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_diff_obj_attr_u.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_diff_type_e.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_diff_u.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_discovery_support.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_dup.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_export_synthetic.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_export_xml.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_export_xmlbuffer.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_flags_e.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_get_allowed_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_get_allowed_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_get_complete_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_get_complete_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_get_depth.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_get_flags.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_get_online_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_get_topology_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_get_topology_nodeset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_get_userdata.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_ignore_all_keep_structure.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_ignore_type.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_ignore_type_keep_structure.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_init.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_insert_misc_object_by_cpuset.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_insert_misc_object_by_parent.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_is_thissystem.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_load.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_membind_support.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_restrict.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_set_custom.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_set_distance_matrix.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_set_flags.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_set_fsroot.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_set_pid.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_set_synthetic.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_set_userdata.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_set_userdata_export_callback.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_set_userdata_import_callback.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_set_xml.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_set_xmlbuffer.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_support.3
rm -f %{buildroot}/usr/share/man/man3/hwloc_topology_t.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_advanced_io.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_api_version.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_bitmap.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_configuration.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_cpubinding.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_creation.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_cuda.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_cudart.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_custom.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_diff.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_distances.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_gl.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_glibc_sched.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_helper_ancestors.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_helper_distribute.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_helper_find_cache.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_helper_find_covering.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_helper_find_inside.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_helper_find_misc.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_helper_nodeset_convert.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_helper_topology_sets.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_intel_mic.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_levels.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_linux.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_linux_libnuma_bitmask.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_linux_libnuma_ulongs.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_membinding.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_myriexpress.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_nvml.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_object_sets.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_object_strings.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_object_types.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_objects.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_opencl.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_openfabrics.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_syntheticexport.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_tinker.3
rm -f %{buildroot}/usr/share/man/man3/hwlocality_xmlexport.3
rm -f %{buildroot}/usr/share/man/man7/hwloc.7

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhwloc.so.5
/usr/lib64/libhwloc.so.5.7.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-hwloc-soname5/COPYING
