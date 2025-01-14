%define major 5
%define libname %mklibname mpcdec %{major}
%define devname %mklibname mpcdec -d

%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	Portable Musepack decoder library
Name:		libmpcdec
Version:	1.2.6
Release:	25
License:	BSD
Group:		System/Libraries
Url:		https://www.musepack.net/
Source0:	http://files.musepack.net/source/%{name}-%{version}.tar.bz2

%description
Portable Musepack decoder library.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n %{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libmpcdec.so.%{major}*

%files -n %{devname}
%doc AUTHORS README ChangeLog
%{_includedir}/*
%{_libdir}/*.so
