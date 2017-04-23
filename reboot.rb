reboot_tag = 'reboot_scheduled'

if tagged?(reboot_tag)
  reboot 'reboot_agent' do
    action :request_reboot
    reason 'Agent reboot requested'
  end

  untag(reboot_tag)
end