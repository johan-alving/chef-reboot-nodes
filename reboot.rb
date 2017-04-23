reboot_tag = 'reboot_scheduled'

if tagged?(reboot_tag)
  reboot 'reboot_node' do
    action :request_reboot
    reason 'Reboot requested'
  end

  untag(reboot_tag)
end
