## Windows → Wazuh field mapping

| Concept      | Wazuh field                         |
|-------------|--------------------------------------|
| Event ID    | data.win.system.eventID              |
| Image       | data.win.eventdata.Image             |
| CommandLine | data.win.eventdata.CommandLine       |
| ParentImage | data.win.eventdata.ParentImage       |
| User        | data.win.eventdata.SubjectUserName   |
| Host        | agent.name / data.win.system.computer|
