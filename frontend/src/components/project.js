import React from "react";

const ProjectItem = ({ project, delete_project }) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.link}</td>
            <td>{project.users.join(", ")}</td>
            <td>
                <button onClick={() => delete_project(project.id)} type="button">
                    Delete
                </button>
            </td>
        </tr>
    );
};

const ProjectList = ({ projects, delete_project }) => {
    return (
        <table className="fa-user">
            <thead>
                <td>ID</td>
                <td>Name</td>
                <td>Link</td>
                <td>Users</td>
            </thead>
            <tbody>
                {projects.map((project) => (
                    <ProjectItem project={project} delete_project={delete_project} />
                ))}
            </tbody>
        </table>
    );
};

export default ProjectList;
