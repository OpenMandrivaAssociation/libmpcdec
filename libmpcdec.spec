%define name	libmpcdec
%define version	1.2.5
%define release %mkrel 1
#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

%define major	5
%define libname %mklibname mpcdec %{major}

Name: 	 	%{name}
Summary: 	Portable Musepack decoder library
Version: 	%{version}
Release: 	%{release}

Source:		http://files.musepack.net/source/%{name}-%{version}.tar.bz2
URL:		http://www.musepack.net/
License:	BSD
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Portable Musepack decoder library.

%package -n 	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	%{name}-devel = %{version}-%{release}
Obsoletes: 	%{name}-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
%if %mdkversion <= 1000
%define __libtoolize true
%endif

%configure2_5x

%make
										
%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


