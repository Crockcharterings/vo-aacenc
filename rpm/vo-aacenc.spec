Name:           libvo-aacenc
Version:        0.1.3
Release:        1
Summary:        VisualOn AAC encoder library
Group:          System Environment/Libraries
License:        Apache License, Version 2.0
URL:            http://sourceforge.net/projects/opencore-amr/
Source0:        %{name}-%{version}.tar.gz

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description
This library contains an encoder implementation of the Advanced Audio Coding
(AAC) audio codec. The library is based on a codec implementation by VisualOn
as part of the Stagefright framework from the Google Android project.

%description devel
The %{name}-devel package contains header file for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}/vo-aacenc

%build
autoreconf -i
%configure --enable-static=no
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/vo-aacenc
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
