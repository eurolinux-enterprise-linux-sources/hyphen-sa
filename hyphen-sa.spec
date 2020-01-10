Name: hyphen-sa
Summary: Sanskrit hyphenation rules
%define upstreamid 20110915
Version: 0.%{upstreamid}
Release: 4%{?dist}
#? in a url causes trouble
#http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/tex/hyph-sa.tex?view=co
Source: hyph-sa.tex
Group: Applications/Text
URL: http://tug.org/tex-hyphen
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LPPL
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Patch0: hyphen-sa-cleantex.patch

%description
Sanskrit hyphenation rules.

%prep
%setup -T -q -c -n hyphen-sa
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl hyph-sa.tex hyph_sa_IN.dic UTF-8
echo "Created with substring.pl by substrings.pl hyph-sa.tex hyph_sa_IN.dic UTF-8" > README
echo "Original in-line credits were:" >> README
echo "" >> README
head -n 17 hyph-sa.tex >> README

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sa_IN.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/hyphen/hyph_sa_IN.dic

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110915-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110915-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110915-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Caolan McNamara <caolanm@redhat.com> - 0.20110915-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100531-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Caolan McNamara <caolanm@redhat.com> - 0.20100531-1
- latest version

* Thu Mar 04 2010 Caolan McNamara <caolanm@redhat.com> - 0.20100304-1
- latest version

* Wed Aug 19 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090412-3
- Related: rhbz#517821 drop hyphen-bn alias

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090412-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 03 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090412-1
- latest version

* Mon Apr 06 2009 Caolan McNamara <caolanm@redhat.com> - 0.20081010-1
- initial version
