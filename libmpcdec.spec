%define major 5
%define libname %mklibname mpcdec %{major}
%define develname %mklibname mpcdec -d

Summary:	Portable Musepack decoder library
Name:		libmpcdec
Version:	1.2.6
Release:	%mkrel 2
License:	BSD
Group:		System/Libraries
URL:		http://www.musepack.net/
Source:		http://files.musepack.net/source/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Portable Musepack decoder library.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n %{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname mpcdec 5 -d
Provides:	%mklibname mpcdec 5 -d

%description -n %{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
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

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
