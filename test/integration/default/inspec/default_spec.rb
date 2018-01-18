describe command('curl https://www.google.com') do
  its('stdout') { should match /oved/ }
end

describe port(80) do
  it { should be_listening }
  #its('processes') {should include 'syslog'}
end
